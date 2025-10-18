
Pico 2 has 3 ADC pins: GPIO26-28 named ADC0-2. These can read voltage at 16bit resolution: from 0=0V to $2^{16}=65536$ for 3.3v.

We will now use the potentiometer to control our buzzers



![[PotentionMeter.png.png]]


```python
from machine import Pin, ADC
from time import sleep

pot = ADC(Pin(26))

while True:
  pot_value = pot.read_u16() # read value, 0-65535 across voltage range 0.0v - 3.3v
  print(pot_value)
  sleep(0.1)
```
