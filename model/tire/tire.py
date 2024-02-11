from abc import ABC, abstractmethod

class Tire(ABC):
    def __init__(self, tire_sensors) -> None:
        super().__init__()
        self.tire_sensors = tire_sensors

    @abstractmethod
    def needs_service(self):
        pass
