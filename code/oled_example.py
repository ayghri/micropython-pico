from machine import Pin, SoftI2C
import ssd1306
import time
import math

# You can choose any other combination of I2C pins
i2c = SoftI2C(scl=Pin(5), sda=Pin(4))

oled_width = 128
oled_height = 64
oled = ssd1306.SSD1306_I2C(oled_width, oled_height, i2c)

oled.fill(0)
oled.show()
t = 0.1

while True:
    time.sleep(0.01)
    oled.fill(0)
    for i in range(128):
        val = int(math.floor((1 + math.cos(i * 0.05 + t)) * 32))
        oled.pixel(i, val, 1)
    oled.show()
    t = t + 0.1
