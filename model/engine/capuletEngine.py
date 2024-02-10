from model.engine import Engine

class CapuletEngine(Engine):
    def __init__(self, last_service_miles, current_miles):
        self.current_miles = current_miles
        self.last_service_miles = last_service_miles
    
    def needs_service(self):
        return self.current_miles > (self.last_service_miles + 30000 )