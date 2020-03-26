class Lamp:

    def __init__(self):
        self.state=False

    def set_on(self):
        self.state=True

    def set_off(self):
        self.state=False

    def get_state(self): #Não percebo o porque desta "Função", nao podiamos simplesmente chamar Lamp.state?
        return self.state

class ColorLamp:

    def __init__(self):
        self.color="White" #Default Color
    
    def set_color(self,color):
        self.color=color

    def get_color(self):
        return self.color