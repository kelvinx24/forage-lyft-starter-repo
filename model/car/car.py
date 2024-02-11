from abc import ABC, abstractmethod
from battery.battery import Battery
from engine.engine import Engine

class Car(ABC):
  def __init__(self, name, engine, battery, tires):
    self.name = name
    self.engine = engine
    self.battery = battery
    self.tires = tires

  def needs_service(self):
    return self.engine.needs_service() or self.battery.needs_service() or self.tires.needs_service()
