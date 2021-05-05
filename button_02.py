from machine import Pin
from utime import sleep
#button_1亮綠燈,button_2亮紅燈,二者同時按閃黃燈
led_red = Pin(18, Pin.OUT)
led_amber = Pin(17, Pin.OUT)
led_green = Pin(16, Pin.OUT)
button_1 = Pin(15, Pin.IN, Pin.PULL_UP) #按鈕1接上拉電阻
button_2 = Pin(13, Pin.IN, Pin.PULL_DOWN) #按鈕2接下拉電阻

while True:
    if button_1.value() == 0:
        led_green.value(1)
        led_red.value(0)
    if button_2.value() == 1:
        led_green.value(0)
        led_red.value(1)
    if button_1.value() == 0 and button_2.value() == 1:
        led_green.value(0)
        led_red.value(0)
        for i in range(3):
            led_amber.value(1)
            sleep(0.5)
            led_amber.value(0)
            sleep(0.5)
