from abc import ABC

from Engine import Engine
from Battery import Battery

class Car(ABC):
    def __init__(self, last_service_date, warning_light_is_on,last_service_mileage, current_mileage,current_date):
        self.last_service_date = last_service_date
        self.engine = Engine(last_service_mileage,current_mileage, warning_light_is_on)
        self.battery = Battery(last_service_date,current_date)