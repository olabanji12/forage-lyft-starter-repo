from car import Car # imports Car class from car.py to be able to use the consructor
from batteries import *
from engines import *
from tyres import *


class CarFactory():

    @staticmethod
    def create_calliope(current_date, last_service_date, current_mileage, last_service_mileage, tire_wear):
        engine = Capulet(current_mileage, last_service_mileage)
        battery = Spindler(current_date, last_service_date)
        tyre = Carrigan(tire_wear)
        car = Car(engine, battery,tyre)
        return car

    @staticmethod
    def create_glissade(current_date, last_service_date, current_mileage, last_service_mileage, tire_wear):
        engine = Willoughby(current_mileage, last_service_mileage)
        battery = Spindler(current_date, last_service_date)
        tyre = Carrigan(tire_wear)
        car = Car(engine, battery,tyre)
        return car

    @staticmethod
    def create_palindrome(current_date, last_service_date, warning_light_is_on,tire_wear):
        engine = Sternman(warning_light_is_on)
        battery = Spindler(current_date, last_service_date)
        tyre = Carrigan(tire_wear)
        car = Car(engine, battery,tyre)
        return car

    @staticmethod
    def create_rorschach(current_date, last_service_date, current_mileage, last_service_mileage,tire_wear):
        engine = Willoughby(current_mileage, last_service_mileage)
        battery = Nubbin(current_date, last_service_date)
        tyre = Octoprime(tire_wear)
        car = Car(engine, battery,tyre)
        return car
    
    @staticmethod
    def create_thovex(current_date, last_service_date, current_mileage, last_service_mileage, tire_wear):
        engine = Capulet(current_mileage, last_service_mileage)
        battery = Nubbin(current_date, last_service_date)
        tyre = Octoprime(tire_wear)
        car = Car(engine, battery,tyre)
        return car