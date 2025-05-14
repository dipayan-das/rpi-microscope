import pigpio
from time import sleep

def setup():
    global directionPin
    directionPin = 23
    global stepPin
    stepPin = 24
    global enablePin
    enablePin = 27
    global pi
    pi = pigpio.pi()

def movement():
    print("Moving Stepper")
    pi.write(enablePin, 1)
    pi.set_PWM_dutycycle(stepPin, 128)
    pi.set_PWM_frequency(stepPin, 500)
    print("Setting Duty cycle")

    sleep(1)

    pi.write(directionPin, 1)

    sleep(1)

    pi.write(directionPin, 0)
    print("Changing Direction")

    pi.set_PWM_dutycycle(stepPin, 0)
    pi.write(enablePin, 0)
    # pi.stop()
    return 0
