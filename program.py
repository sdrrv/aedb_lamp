from controler import LampController

if __name__ == "__main__":
    controller = LampController()
    while True:
        line = input()

        if line == "":
            exit(0)
        
        commands = line.split(" ")
        
        if commands[0] == "CL":
            # Create simple lamp with ID
            lamp_id = commands[1]
            controller.create_simple_lamp(lamp_id)
        elif commands[0] == "CCL":
            # Create color lamp with ID
            lamp_color = commands[1]
            lamp_id = commands[2]
            controller.create_color_lamp(lamp_id,lamp_color)
        elif commands[0] == "CLA": 
            # Create an empty lamp array with ID
            lamp_id = commands[1]
            controller.create_lamp_array(lamp_id)
        elif commands[0] == "ALA":
            # Add lamp to array
            lamp_id = commands[1]
            lamp_array_id = commands[2]
            controller.add_lamp_to_array(lamp_array_id,lamp_id)
        elif commands[0] == "RLA":
            # Remove lamp from array
            lamp_id = commands[1]
            lamp_array_id = commands[2]
            controller.remove_lamp_from_array(lamp_array_id,lamp_id)
        elif commands[0] == "S":
            # Get state of ID
            lamp_id = commands[1]
            print(controller.get_lamp_state(lamp_id))
        elif commands[0] == "ON":
            # Set ID on
            lamp_id = commands[1]
            controller.set_lamp_on(lamp_id)
        elif commands[0] == "OFF":
            # Set ID off
            lamp_id = commands[1]
            controller.set_lamp_off(lamp_id)
        else:
            print("Invalid command.")