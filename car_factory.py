from car import Car # imports Car class from car.py to be able to use the consructor
from batteries.nubbin_battery import Nubbin # imports Nubbin class from nubbin_battery.py to be able to use the consructor
from batteries.spindler_battery import Spindler # imports Spindler class from spindler_battery.py to be able to use the consructor
from engines.capulet_engine import Capulet # imports Capulet class from capulet_engine.py to be able to use the consructor
from engines.sternman_engine import Sternman # imports Sternman class from sternman_engine.py to be able to use the consructor
from engines.willoughby_engine import Willoughby # imports Willoughby class from willoughby_engine.py to be able to use the consructor

class CarFactory():

    @staticmethod
    def create_calliope(current_date, last_service_date, current_mileage, last_service_mileage):
        engine = Capulet(current_mileage, last_service_mileage)
        battery = Spindler(current_date, last_service_date)
        car = Car(engine, battery)
        return car

    @staticmethod
    def create_glissade(current_date, last_service_date, current_mileage, last_service_mileage):
        engine = Willoughby(current_mileage, last_service_mileage)
        battery = Spindler(current_date, last_service_date)
        car = Car(engine, battery)
        return car

    @staticmethod
    def create_palindrome(current_date, last_service_date, warning_light_is_on):
        engine = Sternman(warning_light_is_on)
        battery = Spindler(current_date, last_service_date)
        car = Car(engine, battery)
        return car

    @staticmethod
    def create_rorschach(current_date, last_service_date, current_mileage, last_service_mileage):
        engine = Willoughby(current_mileage, last_service_mileage)
        battery = Nubbin(current_date, last_service_date)
        car = Car(engine, battery)
        return car
    
    @staticmethod
    def create_thovex(current_date, last_service_date, current_mileage, last_service_mileage):
        engine = Capulet(current_mileage, last_service_mileage)
        battery = Nubbin(current_date, last_service_date)
        car = Car(engine, battery)
        return car