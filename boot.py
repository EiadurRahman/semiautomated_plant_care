# This file is executed on every boot (including wake-boot from deepsleep)

# ILIBRARIES

#import esp
#esp.osdebug(None)
import os
from machine import Pin, I2C,ADC
import network
#os.dupterm(None, 1) # disable REPL on UART(0)
import gc
#import webrepl
#webrepl.start()
gc.collect()

# VARIABLES DICLARATIONS
adc = ADC(0)
d1 = Pin(5,Pin.OUT)
d5 = Pin(14, Pin.IN , Pin.PULL_UP)
d4 = Pin(2, Pin.OUT)
d6 = Pin(12 , Pin.OUT)
btn = Pin(0, Pin.IN , Pin.PULL_UP)

sta = network.WLAN(network.STA_IF)

def do_connect():
    import network
    ssid = 'ssid'
    pas = 'password'

    sta = network.WLAN(network.STA_IF)
    if not sta.isconnected():
        print('connecting to network...')
        sta.active(True)
        #sta.connect('your wifi ssid', 'your wifi password')
        sta.connect(ssid,pas)
        while not sta.isconnected() and btn.value() == 1:
            d4.off()
            pass
    print('conneted to internet > ',sta.isconnected())
    d4.on()

do_connect()
