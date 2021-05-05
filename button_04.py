from machine import Pin
from utime import sleep
#按鈕按下後,切換紅,綠燈狀態
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
    if button_2.value() == 1:
        state = not state
        led_green.value(state)
        led_red.value(not state)
    sleep(0.01)
#1.觀察紅,綠燈是否正確輪流切換,如何解決
#2.觀察當按鈕持續按下時,紅綠燈的切換狀態