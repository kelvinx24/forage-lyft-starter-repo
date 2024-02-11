from car.car import Car

from engine.capulet_engine import CapuletEngine
from engine.willoughby_engine import WilloughbyEngine
from engine.sternman_engine import SternmanEngine

from battery.spindlerBattery import SpindlerBattery
from battery.nubbinBattery import NubbinBattery
from model.tire.carriganTire import CarriganTire
from model.tire.octoprimeTire import OctoprimeTire

class CarFactory:
    def create_calliope(self, current_date, last_service_date, current_miles, last_service_miles, tire_wear):
        engine = CapuletEngine(current_miles, last_service_miles)
        battery = SpindlerBattery(last_service_date, current_date)
        tires = CarriganTire(tire_wear)
        return Car("Calliope", engine, battery, tires)
    
    def create_glissade(self, current_date, last_service_date, current_miles, last_service_miles, tire_wear):
        engine = WilloughbyEngine(current_miles, last_service_miles)
        battery = SpindlerBattery(last_service_date, current_date)
        tires = OctoprimeTire(tire_wear)   
        return Car("Glissade", engine, battery, tires)
    
    def create_palindrome(self, current_date, last_service_date, current_miles, last_service_miles, tire_wear):
        engine = SternmanEngine(current_miles, last_service_miles)
        battery = SpindlerBattery(last_service_date, current_date)
        tires = CarriganTire(tire_wear)

        return Car("Palindrome", engine, battery, tires)

    def create_rorschach(self, current_date, last_service_date, current_miles, last_service_miles, tire_wear):
        engine = WilloughbyEngine(current_miles, last_service_miles)
        battery = NubbinBattery(last_service_date, current_date)
        tires = OctoprimeTire(tire_wear)   

        return Car("Rorschach", engine, battery, tires)
    
    def create_thovex(self, current_date, last_service_date, current_miles, last_service_miles, tire_wear):
        engine = CapuletEngine(current_miles, last_service_miles)
        battery = NubbinBattery(last_service_date, current_date)
        tires = CarriganTire(tire_wear)

        return Car("Thovex", engine, battery, tires)