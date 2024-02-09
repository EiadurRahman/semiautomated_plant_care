from machine import ADC,Pin
from time import sleep
import dht

hts = dht.DHT11(Pin(4))
# moisture sensor reading
def moist():
    adc_value = ADC(0).read()
    return str(adc_value)

def humd_temp(keyword):
    hts.measure()
    sleep(1)
    if keyword == 'temp':
        return_value = str(hts.temperature())
    elif keyword == 'humd':
        return_value = str(hts.humidity())
    return return_value
