import machine
import utime

led_red = machine.Pin(18, machine.Pin.OUT)
led_amber = machine.Pin(17, machine.Pin.OUT)
led_green = machine.Pin(16, machine.Pin.OUT)

i=1
while True:
    led_amber.value(not ((i%4) and (i+2)%4))
    led_green.value(not (i+1)%4)
    led_red.value(not (i+3)%4)    
    utime.sleep(1 if (i%2==0 or i%4==0) else 2)
    i+=1