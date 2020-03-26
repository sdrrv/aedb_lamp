from models import Lamp
class LampController:

    def __init__(self):
        self.lamp= Lamp()

    def turn_on(self):
        self.lamp.set_on()

    def turn_off(self):
        self.lamp.set_off()

    def is_on(self):
        return self.lamp.get_state()
