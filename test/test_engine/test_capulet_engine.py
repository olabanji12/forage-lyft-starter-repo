import unittest

from engines.capulet_engine import Capulet


class TestCapuletEngine(unittest.TestCase):
    def test_needs_service_true(self):
        current_mileage = 30001
        last_service_mileage = 0
        engine = Capulet(current_mileage, last_service_mileage)
        self.assertTrue(engine.needs_service())

    def test_needs_service_false(self):
        current_mileage = 30000
        last_service_mileage = 0
        engine = Capulet(current_mileage, last_service_mileage)
        self.assertFalse(engine.needs_service())