from models import Lamp, all_lamps, ColorLamp, LampArray
class LampController:

    def __init__(self):
        self.all_lamps = all_lamps()

    def turn_on(self,lamp):
        lamp.set_on()

    def turn_off(self,lamp):
        lamp.set_off()

    def is_on(self,lamp):
        return lamp.get_state()
    
    def Create_simple_lamp(self):
        pass

