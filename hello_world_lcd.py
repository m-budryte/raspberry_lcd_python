#!/usr/bin/env python

import I2C_LCD_driver
import time
mylcd = I2C_LCD_driver.lcd()
print(mylcd)


while True:
    mylcd.lcd_display_string("HEY BITCH", 1)
