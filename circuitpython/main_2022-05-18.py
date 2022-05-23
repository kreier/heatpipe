# Measuring temperature with DS18B20 - 2022-05-18

import time
import board
from adafruit_onewire.bus import OneWireBus
ow_bus = OneWireBus(board.D2)

devices = ow_bus.scan()
for device in devices:
    print("ROM = {} \tFamily = 0x{:02x}".format([hex(i) for i in device.rom], device.family_code))

import adafruit_ds18x20


sensor0 = adafruit_ds18x20.DS18X20(ow_bus, devices[0])
sensor1 = adafruit_ds18x20.DS18X20(ow_bus, devices[1])
sensor2 = adafruit_ds18x20.DS18X20(ow_bus, devices[2])

while True:
    print('Temperature: {0:0.3f} °C'.format(sensor0.temperature))
    print('Temperature: {0:0.3f} °C'.format(sensor1.temperature))
    print('Temperature: {0:0.3f} °C'.format(sensor2.temperature))
    print('.')
    time.sleep(1.0)


