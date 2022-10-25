import unittest
from tyres.carrigan_tyre import Carrigan

class TestCarriganTyre(unittest.TestCase):
    def test_needs_service_true(self):
        tire_wear = [0.5,0.5,0.5,0.9]
        tire = Carrigan(tire_wear)
        self.assertTrue(tire.needs_service())
    
    def test_needs_service_false(self):
        tire_wear = [0.5,0.5,0.5,0.4]
        tire = Carrigan(tire_wear)
        self.assertFalse(tire.needs_service())