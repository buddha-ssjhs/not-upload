from machine import Pin
from utime import sleep

led_red = Pin(18, Pin.OUT)
led_amber = Pin(17, Pin.OUT)
led_green = Pin(16, Pin.OUT)
buzzer = Pin(10, Pin.OUT)
button_1 = Pin(15, Pin.IN, Pin.PULL_UP) #按鈕1接上拉電阻(一端接GP15,一端接GND)

def trafficlight():
    led_red.value(1)
    sleep(2)
    led_red.value(0)
    led_amber.value(1)
    sleep(1)
    led_amber.value(0)
    led_green.value(1)
    sleep(2)
    led_green.value(0)
    led_amber.value(1)
    sleep(1)
    led_amber.value(0)

while True:
    if button_1.value() == 1:
        trafficlight()
    else:
        print("行人優先")
        led_red.value(1)
        for i in range(5):
            buzzer.value(1)
            sleep(0.2)
            buzzer.value(0)
            sleep(0.2)
        led_red.value(0)