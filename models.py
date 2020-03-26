class Lamp:

    def __init__(self):
        self.state=False

    def set_on(self):
        self.state=True

    def set_off(self):
        self.state=False
        
    def get_state(self): #Não percebo o porque desta "Função", nao podiamos simplesmente chamar Lamp.state?
        return self.state