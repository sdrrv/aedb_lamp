from controler import LampController

if __name__ == '__main__':

    controller = LampController()

    while True:
        line = input()
        #--------------------------------
        if line =="":
            exit(0)
        elif line=="ON":
            controller.turn_on()
        elif line=="OFF":
            controller.turn_off()
        elif line=="STATE":  
            if(controller.is_on()):
                print("On")
            else:
                print("Off")
        #-------------------------------- 
    