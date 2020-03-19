from models import Lamp

class LampController:
    def __init__(self):
        self.lamp = Lamp()

    def turn_on(self):
        self.lamp.turn_on()

    def turn_off(self):
        pass

    def is_on(self):
        return self.lamp.state