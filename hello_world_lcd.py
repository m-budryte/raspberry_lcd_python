#!/usr/bin/env python

import RPi_I2C_driver
from time import *

mylcd = RPi_I2C_driver.lcd()

mylcd.lcd_display_string("This is how you", 1)
sleep(1)

mylcd.lcd_clear()

mylcd.lcd_display_string("clear the screen", 1)
sleep(1)

mylcd.lcd_clear()
