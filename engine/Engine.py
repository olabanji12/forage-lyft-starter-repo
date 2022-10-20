from abc import abstractmethod


class Engine():
    def __init__(self, last_service_mileage, current_mileage, warning_light_is_on):
        self.last_service_mileage = last_service_mileage
        self.current_mileage = current_mileage
        self.warning_light_is_on = warning_light_is_on
    

    @abstractmethod
    def needs_service(self):
        pass
