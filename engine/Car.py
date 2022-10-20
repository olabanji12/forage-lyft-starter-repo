from abc import ABC

from engine.Engine import Engine


class Car(ABC):
    def __init__(self, last_service_date, warning_light_is_on):
        self.last_service_date = last_service_date
        self.engine = Engine(last_service_date, warning_light_is_on)