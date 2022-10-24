import unittest

from engines.willoughby_engine import Willoughby


class TestWilloughbyEngine(unittest.TestCase):
    def test_needs_service_true(self):
        current_mileage = 60001
        last_service_mileage = 0
        engine = Willoughby(current_mileage, last_service_mileage)
        self.assertTrue(engine.needs_service())

    def test_needs_service_false(self):
        current_mileage = 60000
        last_service_mileage = 0
        engine = Willoughby(current_mileage, last_service_mileage)
        self.assertFalse(engine.needs_service())