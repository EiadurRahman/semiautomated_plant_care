import ThingESP
thing = ThingESP.Client('user_name', 'project_name', 'password')
ThingESP.send_msg('device is back online ')
from time import sleep
import err_log


def handleResponse(query):
    if query == 'help': # help tempate
        help_template = """
To check moisture status  : moisture status
To check relative humidity : humidity
To check relative temperature : temperature
To start the pump : start pump
"""
        ThingESP.send_msg(help_template)
    # check moisture status
    elif query == 'moisture status' :
        value = round((adc.read()/1024)*100)
        ThingESP.send_msg('soil moisture is : {0}%'.format(value))
        
    # write a condition for it to say if truning motor is nesseary or not if usr ask to turn on motor
    elif query == 'start pump' :
        if adc.read() > 800: # to check if starting a ,otor is needed
            value = round((adc.read()/1024)*100) # convert into persentage
            ThingESP.send_msg(' moisture level is at {0}%, watering is unnessery'.format(value))
        else:
            ThingESP.send_msg('starting the pump')
            d1.on()
    else:
        return 'no task is set for [%s]'%query
# error handling loop
while True :
    try :
        thing.setCallback(handleResponse).start()
    except Exception as err:
        print(err)
        err_log.log(err) # log error msgs into err.txt file
    print('END_TASK')
d4.off()

