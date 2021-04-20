from machine import Pin
import utime

#led_red = Pin(18, Pin.OUT)
led_amber = Pin(17, Pin.OUT)
#led_green = Pin(16, Pin.OUT)
button_1 = Pin(15, Pin.IN, Pin.PULL_UP) #按鈕1接上拉電阻(一端接GP15,一端接GND)

led_amber.value(0)

while True:
    if button_1.value() == 0:
        for i in range(3):
            led_amber.value(1)
            utime.sleep(0.5)
            led_amber.value(0)
            utime.sleep(0.5)
#test
    
