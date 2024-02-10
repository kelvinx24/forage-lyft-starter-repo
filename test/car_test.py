import datetime
import unittest
from model.battery.nubbinBattery import NubbinBattery
from model.battery.spindlerBattery import SpindlerBattery
from model.car.carFactory import CarFactory

from model.engine.capuletEngine import CapuletEngine
from model.engine.sternamEngine import SternamEngine
from model.engine.willoughbyEngine import WilloughbyEngine


class TestEngine(unittest.TestCase):
    def test_capulet_needs_service(self):
        engine1 = CapuletEngine(0, 31000)
        self.assertTrue(engine1.needs_service())

        engine2 = CapuletEngine(45000, 80000)
        self.assertTrue(engine2.needs_service())

        engine3 = CapuletEngine(1, 30002)
        self.assertTrue(engine3.needs_service())



    def test_capulet_no_service(self):
        engine1 = CapuletEngine(0, 0)
        self.assertFalse(engine1.needs_service())

        engine2 = CapuletEngine(50000, 75000)
        self.assertFalse(engine2.needs_service())

        engine3 = CapuletEngine(0, 30000)
        self.assertFalse(engine3.needs_service())


    def test_capulet_invalid(self):
        engine1 = CapuletEngine(-100, 0)
        self.assertRaises(ValueError, engine1.needs_service)

        engine2 = CapuletEngine(1100, -90121)
        self.assertRaises(ValueError, engine2.needs_service)

        engine3 = CapuletEngine(-100, -40000)
        self.assertRaises(ValueError, engine3.needs_service)

        engine4 = CapuletEngine(40000, 8000)
        self.assertRaises(ValueError, engine4.needs_service)


    def test_willoughby_needs_service(self):
        engine1 = WilloughbyEngine(0, 61000)
        self.assertTrue(engine1.needs_service())

        engine2 = WilloughbyEngine(45000, 110000)
        self.assertTrue(engine2.needs_service())

        engine3 = WilloughbyEngine(1, 60002)
        self.assertTrue(engine3.needs_service())


    def test_willoughby_no_service(self):
        engine1 = WilloughbyEngine(0, 0)
        self.assertFalse(engine1.needs_service())

        engine2 = WilloughbyEngine(50000, 75000)
        self.assertFalse(engine2.needs_service())

        engine3 = WilloughbyEngine(0, 60000)
        self.assertFalse(engine3.needs_service())


    def test_willoughby_invalid(self):
        engine1 = WilloughbyEngine(-100, 0)
        self.assertRaises(ValueError, engine1.needs_service)

        engine2 = WilloughbyEngine(1100, -90121)
        self.assertRaises(ValueError, engine2.needs_service)

        engine3 = WilloughbyEngine(-100, -40000)
        self.assertRaises(ValueError, engine3.needs_service)

        engine4 = WilloughbyEngine(40000, 8000)
        self.assertRaises(ValueError, engine4.needs_service)

    def test_sternam_needs_service(self):
        engine1 = SternamEngine(True)

        self.assertTrue(engine1.needs_service())

    def test_sternam_no_service(self):
        engine1 = SternamEngine(False)
        self.assertFalse(engine1.needs_service())

class TestBattery(unittest.TestCase):
    def test_spindler_needs_service(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 3)
        
        battery1 = SpindlerBattery(last_service_date, today)
        self.assertTrue(battery1.needs_service())
    
    def test_spindler_no_service(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 2)

        battery1 = SpindlerBattery(last_service_date, today)
        self.assertFalse(battery1.needs_service())

        last_service_date = today.replace(year=today.year - 1)
        battery2 = SpindlerBattery(last_service_date, today)
        self.assertFalse(battery2.needs_service())

        battery3 = SpindlerBattery(today, today)
        self.assertFalse(battery3.needs_service())

    def test_spindler_invalid(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 2)

        battery1 = SpindlerBattery(today, last_service_date)
        self.assertFalse(battery1.needs_service())

    def test_nubbin_needs_service(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 5)
        
        battery1 = NubbinBattery(last_service_date, today)
        self.assertTrue(battery1.needs_service())
    
    def test_nubbin_no_service(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 4)

        battery1 = NubbinBattery(last_service_date, today)
        self.assertFalse(battery1.needs_service())

        last_service_date = today.replace(year=today.year - 1)
        battery2 = NubbinBattery(last_service_date, today)
        self.assertFalse(battery2.needs_service())

        battery3 = NubbinBattery(today, today)
        self.assertFalse(battery3.needs_service())

    def test_spindler_invalid(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 2)

        battery1 = NubbinBattery(today, last_service_date)
        self.assertFalse(battery1.needs_service())

class TestCar(unittest.TestCase):
    def test_cars_needs_service(self):
        factory = CarFactory()

        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 3)
        calli1 = factory.create_calliope(today, last_service_date, 0, 0)
        self.assertTrue(calli1.needs_service())

        calli2 = factory.create_calliope(today, today, 0, 100000)
        self.assertTrue(calli2.needs_service())

        calli3 = factory.create_calliope(today, last_service_date, 0, 100000)
        self.assertTrue(calli3.needs_service())

    def test_cars_no_service(self):
        factory = CarFactory()
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 1)
        calli1 = factory.create_calliope(today, last_service_date, 0, 0)
        self.assertFalse(calli1.needs_service())

        calli2 = factory.create_calliope(today, today, 0, 2000)
        self.assertFalse(calli2.needs_service())

        calli3 = factory.create_calliope(today, last_service_date, 0, 200)
        self.assertFalse(calli3.needs_service())