import unittest
from tyres.octoprime_tyre import Octoprime

class TestOctoprimeTyre(unittest.TestCase):
    def test_needs_service_true(self):
        tire_wear = [0.9,0.9,0.8,0.6]
        tire = Octoprime(tire_wear)
        self.assertTrue(tire.needs_service())
    
    def test_needs_service_false(self):
        tire_wear = [0.5,0.5,0.5,0.5]
        tire = Octoprime(tire_wear)
        self.assertFalse(tire.needs_service())
