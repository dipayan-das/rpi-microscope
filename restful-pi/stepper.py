import pigpio
from time import sleep

def setup():
    
    global directionPin
    directionPin = 23
    global stepPin
    stepPin = 24

    global directionPin2
    directionPin2 = 4
    global stepPin2
    stepPin2 = 17

    global enablePin
    enablePin = 27
    global pi
    pi = pigpio.pi()

def movement(dir):
    if dir == 'base':
        print("base")
        s = stepPin2
        d = directionPin2
    else:
        print("top")
        s = stepPin
        d = directionPin
    print(s," ",d)
    print("Moving Stepper")
    pi.write(enablePin, 1)
    pi.set_PWM_dutycycle(s, 128)
    pi.set_PWM_frequency(s, 500)
    print("Setting Duty cycle")

    sleep(1)

    pi.write(d, 1)

    sleep(1)

    pi.write(d, 0)
    print("Changing Direction")

    pi.set_PWM_dutycycle(s, 0)
    pi.write(enablePin, 0)
    sleep(1)
    # pi.stop()
    return 0
