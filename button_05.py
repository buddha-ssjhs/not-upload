from machine import Pin
from utime import sleep

led_red = Pin(18, Pin.OUT)
led_amber = Pin(17, Pin.OUT)
led_green = Pin(16, Pin.OUT)
button_1 = Pin(15, Pin.IN, Pin.PULL_UP) #外側按鈕接上拉電阻
button_2 = Pin(13, Pin.IN, Pin.PULL_DOWN) #內側按鈕拉下拉電阻

led_red.value(0)
led_amber.value(0)
led_green.value(0)
state = False
button_On = True #button_03持續按下按鈕時,紅綠燈不斷切換的解決方式,使用旗標
while True:
    if button_2.value() == 1 and button_On ==1:
        state = not state
        led_green.value(state)
        led_red.value(not state)
        button_On = not button_On
    if button_2.value()==0 and button_On ==0:
        button_On = not button_On