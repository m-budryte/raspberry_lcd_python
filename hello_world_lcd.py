#!/usr/bin/env python

import I2C_LCD_driver
import * from time

mylcd = I2C_LCD_driver.lcd()

mylcd.lcd_display_string("Hello World!", 1)
