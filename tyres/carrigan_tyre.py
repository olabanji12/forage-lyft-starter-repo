from tyres.tyre import Tyre
import numpy as np

class Carrigan(Tyre):
    def __init__(self, tire_wear ):
        self.tire_wear = tire_wear
    
    def needs_service(self):
        for tire in self.tire_wear:
            if tire >= 0.9:
                return True
        return False