from models import Lamp, all_lamps, ColorLamp, LampArray, all_lamp_arrays
class LampController:

    def __init__(self):
        self.all_lamps = all_lamps()
        self.all_lamp_arrays = all_lamp_arrays()
    def turn_on(self,lamp):
        lamp.set_on()

    def turn_off(self,lamp):
        lamp.set_off()

    def is_on(self,lamp):
        return lamp.get_state()
    
    def create_simple_lamp(self,lamp_id):
        self.all_lamps.append(Lamp(),lamp_id)
    
    def create_color_lamp(self,lamp_id,color):
        self.all_lamps.append(ColorLamp(),lamp_id)
        self.all_lamps.lamp_list[lamp_id].set_color(color)

    def create_lamp_array(self,array_id):
        self.all_lamp_arrays.append(LampArray(),array_id)
    
    def add_lamp_to_array(self,array_id,lamp_id):
        self.all_lamp_arrays.lamp_arrays[array_id].append(self.all_lamps.get_lamp(lamp_id))
    
