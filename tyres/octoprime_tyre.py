from tyres.tyre import Tyre
import numpy as np

class Octoprime(Tyre):
    def __init__(self, tire_wear):
        self.tire_wear = tire_wear
    
    def needs_service(self):
        return sum(self.tire_wear) >= 3.0