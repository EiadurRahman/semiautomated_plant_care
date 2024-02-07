from machine import ADC
from time import sleep

# moisture sensor reading
def moist():
    adc_value = ADC(0).read()
    return str(adc_value)
    
# humidity sensor reading

# temperature sensor reading
