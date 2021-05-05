from machine import Pin
from utime import sleep

led_red = machine.Pin(18, machine.Pin.OUT)
led_amber = machine.Pin(17, machine.Pin.OUT)
led_green = machine.Pin(16, machine.Pin.OUT)

i=1
while True:
    led_green.value(not i%3)
    led_amber.value(not (i+1)%3)
    led_red.value(not (i+2)%3)
    sleep(1)
    i+=1