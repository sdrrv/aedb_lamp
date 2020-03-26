class Lamp:

    def __init__(self):
        self.state=False

    def set_on(self):
        self.state=True

    def set_off(self):
        self.state=False
        
    def get_state(self):
        return self.state

class ColorLamp(Lamp):
    
    def __init__(self):
        Lamp.__init__(self)
        self.color='White'

    def get_color(self):
        return self.color

    def set_color(self,color):
        self.color=color          