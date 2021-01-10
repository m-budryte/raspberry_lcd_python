#!/usr/bin/env python

import RPi_I2C_driver
from time import *

mylcd = RPi_I2C_driver.lcd()

input_value = input("Enter your value: ") 

mylcd.lcd_display_string("hiiiiii", 1)
sleep(1)

mylcd.lcd_clear()
