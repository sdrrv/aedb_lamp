from models import Lamp

class LampController:
    def __init__(self):
        self.Lamp= Lamp()

    def turn_on(self):
        self.Lamp.set_on()

    def turn_off(self):
        self.Lamp.set_off()

    def is_on(self):
        return self.Lamp.get_state()
