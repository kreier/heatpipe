# Evan's script for analog in A1 and out on A2

import time
import board
import pwmio
from analogio import AnalogIn, AnalogOut
from adafruit_motor import servo

analog_in = AnalogIn(board.A1)
analog_out = AnalogOut(board.A0)


def get_voltage(pin):
    return (pin.value * 3.3) / 65536


# create a PWMOut object on Pin A2.
pwm = pwmio.PWMOut(board.A2, duty_cycle=2 ** 15, frequency=50)

# Create a servo object, my_servo.
my_servo = servo.Servo(pwm)

while True:
    for angle in range(0, 180, 5):  # 0 - 180 degrees, 5 degrees at a time.
        my_servo.angle = angle
        time.sleep(0.05)
        #print((get_voltage(analog_in),))
        #print(my_servo.angle)
    for angle in range(180, 0, -5):  # 180 - 0 degrees, 5 degrees at a time.
        my_servo.angle = angle
        time.sleep(0.05)
        #print((get_voltage(analog_in),))
        #print(my_servo.angle)



