class Lamp:

    def __init__(self,lamp_id):
        self.state=False
        self.id = lamp_id

    def set_on(self):
        self.state=True

    def set_off(self):
        self.state=False

    def get_state(self): #Não percebo o porque desta "Função", nao podiamos simplesmente chamar Lamp.state?
        return self.state

class ColorLamp(Lamp):
    def __init__(self,lamp_id):
        Lamp.__init__(self,lamp_id)
        self.color = "White" #Default Color
        
    def set_color(self, color):
        self.color = color

    def get_color(self):
        return self.color

class LampArray:
    def __init__(self):
        self.conjunto = []
    
    def append(self, lamp):
        self.conjunto.append(lamp)
    
    def turn_on(self):
        for lamp in self.conjunto:
            lamp.set_on()
    
    def turn_off(self):
        for lamp in self.conjunto:
            lamp.set_off()
    
    def get_conjunto_states(self):
        result = []
        for lamp in self.conjunto:
            result.append(lamp.get_state())
        return result

    def remove_lamp(self,lamp_id):
        for lamp in self.conjunto:
            if lamp.id == lamp_id:
                self.conjunto.remove(lamp)

class all_lamps:
    def __init__(self):
        self.lamp_list={}
    
    def append(self,lamp,lamp_id):
        self.lamp_list[lamp_id]=lamp
    
    def remove(self,lamp_id):
        self.lamp_list.pop(lamp_id)
    
    def get_lamp(self,lamp_id):
        return self.lamp_list[lamp_id]

class all_lamp_arrays:
    def __init__(self):
        self.lamp_arrays={}
    
    def append(self,lamp_array,array_id):
        self.lamp_arrays[array_id]=lamp_array
    
    def remove(self,array_id):
        self.lamp_arrays.pop(array_id)