from machine import Pin
from utime import sleep
#使用button_1與button_2模擬雙切開關
led_red = Pin(18, Pin.OUT)
led_amber = Pin(17, Pin.OUT)
led_green = Pin(16, Pin.OUT)
button_1 = Pin(15, Pin.IN, Pin.PULL_UP) #外側按鈕接上拉電阻
button_2 = Pin(13, Pin.IN, Pin.PULL_DOWN) #內側按鈕拉下拉電阻

led_red.value(0)
led_amber.value(0)
led_green.value(0)
state = False

while True:
    if button_1.value() == 0 :
        state = not state
        led_amber.value(state)
    if button_2.value() == 1 :
        state = not state
        led_amber.value(state)