from model.tire.tire import Tire


class CarriganTire(Tire):
    def __init__(self, tire_sensors) -> None:
        super().__init__(tire_sensors)

    def needs_service(self):
        for t in self.tire_sensors:
            if t >= 0.9:
                return True
        
        return False