from machine import Pin, ADC, PWM

import time

pot = ADC(Pin(26))
buzzer = PWM(Pin(15))
buzzer.freq(1_000)

def set_volts(v):
    v = max(0.0, min(3.3, v))
    duty = int(v/3.3 * 65535)
    buzzer.duty_u16(duty)

while True:
    pot_value = pot.read_u16()
    print(pot_value)
    set_volts(3.3*pot_value/66_000)

    time.sleep(0.01)
