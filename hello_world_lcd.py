#!/usr/bin/env python

import RPi_I2C_driver
from time import *

mylcd = RPi_I2C_driver.lcd()

val = input("Enter your value: ") 
print(val) 

mylcd.lcd_display_string(str(val), 1)
sleep(1)

mylcd.lcd_clear()
