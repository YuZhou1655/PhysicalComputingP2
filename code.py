import time
import board
import digitalio
import neopixel
import analogio
import pwmio

from adafruit_motor import servo

pwm = pwmio.PWMOut(board.A1, duty_cycle=2 ** 15, frequency=50)

my_servo = servo.Servo(pwm)

# BUTTON_A is an reference to the 2 buttons on the Circuit Python Express
switch = digitalio.DigitalInOut(board.A0)
switch.direction = digitalio.Direction.INPUT
analogin = analogio.AnalogIn(board.A7)

# pull controls the electrical behavoir of the pin
# The standard Pull.DOWN as electricity flows through the pin, switch.value = False(LOW), When the button is pressed, switch.value = True(HIGH)
switch.pull = digitalio.Pull.DOWN
# Pull.UP inverses the behavior and enables the built in resistor

pixels = neopixel.NeoPixel(board.NEOPIXEL, 10, brightness=1, auto_write=False)

while True:
    # str() converts variable output into string
    # When adding string + string you get a sentence
    # string + number, string + bool, string + variable wont work
    potVoltage = analogin.value
    potVoltage = (analogin.value * 3.3) /65536
    time.sleep(0.1)
    print("Current switch value: " + str(switch.value))
    if switch.value == True:
        if potVoltage >= 3.1:
            my_servo.angle = 0
            pixels.fill((0,0,0))
            pixels.show()
            print("Analog Voltage:" + str(potVoltage))
        if potVoltage <= 3.099:
            my_servo.angle = 180
            pixels.fill((255,255,255))
            pixels.show()
            print("Analog Voltage:" + str(potVoltage))
    else:
        pixels.fill((0,0,0))
        pixels.show()
        my_servo.angle = 90

    time.sleep(0.1)  # debounce delay
