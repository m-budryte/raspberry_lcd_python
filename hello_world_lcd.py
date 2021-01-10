#!/usr/bin/env python

import I2C_LCD_driver
import time
mylcd = I2C_LCD_driver.lcd()
print(mylcd)


while True:
    mylcd.backlight(0)
    sleep(5)
    mylcd.backlight(1)