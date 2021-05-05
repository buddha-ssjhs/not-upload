from machine import Pin
from utime import sleep
import trafficlight as tr

led_red = Pin(18, Pin.OUT)
led_amber = Pin(17, Pin.OUT)
led_green = Pin(16, Pin.OUT)
buzzer = Pin(10, Pin.OUT)
PIR = Pin(2, Pin.IN, Pin.PULL_DOWN)#ACC端需接5V電源

while True:
    PIR.irq(trigger=Pin.IRQ_RISING,handler=tr.pedestrianfirst)
    tr.trafficlight()