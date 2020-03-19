from controllers import LampController

if __name__ == "__main__":
    controller = LampController()
    
    while True:
        line = input()

        if line == "":
            exit(0)

        if line == "ON":
            controller.turn_on()
            print("Lamp is on.")
        elif line == "OFF":
            controller.turn_off()
            print("Lamp is off.")
        elif line == "STATE":
            is_on = controller.is_on() # boolean
            if is_on:
                print("Lamp is on.")
            else:
                print("Lamp is off.")