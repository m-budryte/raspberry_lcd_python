#!/usr/bin/env python

import RPi_I2C_driver
from time import *

mylcd = RPi_I2C_driver.lcd()

console_input = input("enter your mesage: ")

mylcd.lcd_display_string(console_input, 1)
sleep(1)

mylcd.lcd_clear()

mylcd.lcd_display_string("clear the screen", 1)
sleep(1)

mylcd.lcd_clear()
