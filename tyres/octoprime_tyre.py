from tyre import Tyre
import numpy as np

class Octoprime(Tyre):
    def __init__(self, tire_wear = np.zeros(4, dtype=float)):
        self.tire_wear = tire_wear
    
    def needs_service(self):
        sum = 0.0
        for i in self.tire_wear:
            sum += self.tire_wear[i]
        return sum >= 3 