#使用中斷 IRQ
#設定當PIR偵測到人體時(電壓 RISING),啟動中斷 IRQ
from machine import Pin
from utime import sleep

led_red = Pin(18, Pin.OUT)
led_amber = Pin(17, Pin.OUT)
led_green = Pin(16, Pin.OUT)
buzzer = Pin(10, Pin.OUT)
PIR = machine.Pin(2, machine.Pin.IN, machine.Pin.PULL_DOWN)#ACC端需接5V電源

def trafficlight():
    led_red.value(1)
    sleep(2)
    led_red.value(0)
    led_amber.value(1)
    sleep(2)
    led_amber.value(0)
    led_green.value(1)
    sleep(2)
    led_green.value(0)
    led_amber.value(1)
    sleep(2)
    led_amber.value(0)
def pedestrianfirst(pin):
    PIR.irq(handler=None)
    print("行人優先")
    led_red.value(1)
    led_amber.value(0)
    led_green.value(0)
    for i in range(5):
        buzzer.value(1)
        sleep(0.2)
        buzzer.value(0)
        sleep(0.2)
    led_red.value(0)

while True:
    PIR.irq(trigger=Pin.IRQ_RISING,handler=pedestrianfirst)
    trafficlight()