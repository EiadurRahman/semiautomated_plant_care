import ThingESP
thing = ThingESP.Client('user_name', 'project_name', 'password')
ThingESP.send_msg('device is back online ')
from time import sleep
import err_log


def handleResponse(query):
    if query == 'help': # help tempate
        help_template = """
To check moisture status  : moisture status / ms
To check relative humidity : humidity / humd
To check relative temperature : temperature / temp
To start the pump : start pump / sp
"""
        return (help_template)
    # check moisture status
    elif query in ['moisture status','ms']:
        value = round((adc.read()/1024)*100)
        return ('soil moisture is : {0}%'.format(value))
        
    # motor handling 
    elif query in  ['start pump','sp'] :
        if adc.read() > 800: # to check if starting a ,otor is needed
            value = round((adc.read()/1024)*100) # convert into persentage
            return (' moisture level is at {0}%, watering is unnessery'.format(value))
        else:
            return ('starting the pump')
            d1.on()
    # DHT11 sensor 
    elif query in ['humidity','temperature','humd','temp']:
        if query in ['humidity','humd']:
            humidity = reading.humd_temp('humd')
            return ('humidity : {}%'.format(humidity))
        elif query in [ 'temperature', 'temp']:
            temp = reading.humd_temp('temp')
            return ('temperature : {}.C'.format(temp))
    # returns errors stored in err.txt file
    elif query == 'read_err':
        return err_log.read_err()
    else:
        return 'no task is set for {}'.format(query)
# error handling loop
while True :
    try :
        thing.setCallback(handleResponse).start()
    except Exception as err:
        print(err)
        err_log.log(err) 
        d4.off()
        sleep(1)
        d4.on()
        machine.reset() # resets the device
