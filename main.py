from machine import Pin
import time

entrance = Pin(34, Pin.IN, Pin.PULL_UP)  
exit = Pin(35, Pin.IN, Pin.PULL_UP)     

led_pins = [2, 4, 5, 13, 14, 16, 17, 18]  
leds = [Pin(pin, Pin.OUT) for pin in led_pins]

car_count = 0  

def show_leds(n):
    for i, led in enumerate(leds):
        led.value(1 if i < n else 0)

while True:
    if not entrance.value():
        if car_count < 8:
            car_count += 1
            print(car_count," Car Intered" )
            show_leds(car_count)
        else:
            print("Full")
        time.sleep(0.3)
        while not entrance.value():
            pass

    if not exit.value():
        if car_count > 0:
            car_count -= 1
            print(car_count," Went out" )
            show_leds(car_count)
        else:
            print("Empty garage")
        time.sleep(0.3)
        while not exit.value():
            pass

    time.sleep(0.01) 
