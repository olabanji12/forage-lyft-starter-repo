from tyre import Tyre
import numpy as np

class Carrigan(Tyre):
    def __init__(self, tire_wear = np.zeros(4, dtype=float)):
        self.tire_wear = tire_wear
    
    def needs_service(self):
        for i in self.tire_wear:
            if self.tire_wear[i] >= 0.9:
                return True
        return False