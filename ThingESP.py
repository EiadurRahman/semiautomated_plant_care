import ujson as json
import network
import time
import machine
from machine import Pin
import urequests as requests
import reading
from umqtt.simple import MQTTClient


d4 = Pin(2, Pin.OUT) # status led
d1 = Pin(5,Pin.OUT) # motor/pump output
thingesp_server = 'thingesp.siddhesh.me'


class Client:
    def __init__(self, username, projectName, password):
        self.username = username
        self.projectName = projectName
        self.password = password
        self.initalized = False
        self.mqtt_client = MQTTClient(client_id=projectName + "@" + username,
                                      server=thingesp_server, port=1893, user=projectName + "@" + username, password=password,keepalive=0)
        self.mqtt_client.set_callback(self.on_message)
        self.mqtt_client.connect()

        
    def setCallback(self, func):
        self.callback_func = func
        self.initalized = True
        return self

    def on_message(self, client, msg):
        if self.initalized != True:
            print('Please set the callback func!')
            return
        else:
            payload = json.loads(msg.decode("utf-8"))
#             print(payload)
            if payload['action'] == 'query':
                out = self.callback_func(payload['query'].lower()) or ""
                sendr = {
                    "msg_id": payload['msg_id'], "action": "returned_api_response", "returned_api_response": out}
                self.mqtt_client.publish(
                    self.projectName + "/" + self.username, json.dumps(sendr))

    def start(self):
        self.mqtt_client.set_callback(self.on_message)
        self.mqtt_client.subscribe(self.projectName + "/" + self.username)
        
        one_time_msg_send = False # for sending msg for once
        init_time = time.time()
        try:
            while True:
                
                self.mqtt_client.check_msg()   # Pass blocking argument as False
                passed_time = time.time() - init_time
                if passed_time > 300:
                    print('reconnecting....')
                    self.mqtt_client.subscribe(self.projectName + "/" + self.username)
                    init_time = time.time()
                
                # sensor data reading
                value = int(reading.moist())
                if value < 300 and not one_time_msg_send:
                    d1.on()
                    one_time_msg_send = True
                    self.send_msg("Moisture level is low")
                elif value > 1000 and one_time_msg_send:# set value to stop overflow
                    d1.off()
                    one_time_msg_send = False  
                    self.send_msg('Moisture level is restored')
                time.sleep(.1)
        except Exception as err:
            print('error : ',err)
            d1.off()
        time.sleep(0.2)
