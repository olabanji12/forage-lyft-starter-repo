from abc import ABC


class Car(ABC):
    def __init__(self, last_service_date):
        self.last_service_date = last_service_date
    