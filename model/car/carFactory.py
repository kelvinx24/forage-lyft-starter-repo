from car.car import Car

from engine.capulet_engine import CapuletEngine
from engine.willoughby_engine import WilloughbyEngine
from engine.sternman_engine import SternmanEngine

from battery.spindlerBattery import SpindlerBattery
from battery.nubbinBattery import NubbinBattery

class CarFactory:
    def create_calliope(self, current_date, last_service_date, current_miles, last_service_miles):
        engine = CapuletEngine(current_miles, last_service_miles)
        battery = SpindlerBattery(last_service_date, current_date)

        return Car("Calliope", engine, battery)
    
    def create_glissade(self, current_date, last_service_date, current_miles, last_service_miles):
        engine = WilloughbyEngine(current_miles, last_service_miles)
        battery = SpindlerBattery(last_service_date, current_date)

        return Car("Glissade", engine, battery)
    
    def create_palindrome(self, current_date, last_service_date, current_miles, last_service_miles):
        engine = SternmanEngine(current_miles, last_service_miles)
        battery = SpindlerBattery(last_service_date, current_date)

        return Car("Palindrome", engine, battery)

    def create_rorschach(self, current_date, last_service_date, current_miles, last_service_miles):
        engine = WilloughbyEngine(current_miles, last_service_miles)
        battery = NubbinBattery(last_service_date, current_date)

        return Car("Rorschach", engine, battery)
    
    def create_thovex(self, current_date, last_service_date, current_miles, last_service_miles):
        engine = CapuletEngine(current_miles, last_service_miles)
        battery = NubbinBattery(last_service_date, current_date)

        return Car("Thovex", engine, battery)