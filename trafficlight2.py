from machine import Pin
from utime import sleep

led_red = Pin(18, Pin.OUT)
led_amber = Pin(17, Pin.OUT)
led_green = Pin(16, Pin.OUT)

state=True
while True:
    led_amber.value(0)
    led_red.value(state)
    led_green.value(not state)  
    sleep(2)
    led_amber.value(1)
    led_red.value(0)
    led_green.value(0)    
    sleep(1)     
    state = not state