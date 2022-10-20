from Battery import Battery
class Nubbin(Battery):
    def __init__(self, last_service_date, current_date):
        super().__init__(last_service_date, current_date)
    
    def needs_service(self):
        return self.current_date.year - self.last_service_date.year > 4