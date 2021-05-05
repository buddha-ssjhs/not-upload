#使用Thread
#在另一個Thread執行偵測PIR狀態的程式
from machine import Pin
from utime import sleep
import _thread

led_red = Pin(18, Pin.OUT)
led_amber = Pin(17, Pin.OUT)
led_green = Pin(16, Pin.OUT)
buzzer = Pin(10, Pin.OUT)
PIR = machine.Pin(2, machine.Pin.IN, machine.Pin.PULL_DOWN)#ACC端需接5V電源
global PIR_sensor
PIR_sensor = False

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
def pedestrianfirst():
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
def PIR_sensor_thread():
    global PIR_sensor
    while True:
        if PIR.value() == 1:
            PIR_sensor = True
        
_thread.start_new_thread(PIR_sensor_thread, ())
while True:
    trafficlight()
    if PIR_sensor == True:
        pedestrianfirst()
        PIR_sensor = False