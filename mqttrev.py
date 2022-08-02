from paho.mqtt import client as mqtt_client
from http import client
from multiprocessing.connection import wait
import os
from re import X
import random
import sys
import time
import functools
import keyboard
sys.path.append(os.path.join(os.path.dirname(__file__), '../../..'))
from uarm.wrapper import SwiftAPI
swift = SwiftAPI(filters={'hwid': 'USB VID:PID=2341:0042'})
from uarm.swift.protocol import SERVO_BOTTOM, SERVO_LEFT, SERVO_RIGHT, SERVO_HAND
a = 0
rotate = 90
stret = 200
high = 150
val = 90
broker = 'broker.hivemq.com'
port = 1883
topic = [("aielab/rotation",0), ("aielab/toggle" , 0)]

client_id = f'python-mqtt-{random.randint(0, 1000)}'

print("Reset to default position")
def connect_mqtt():
    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            print("Connected to MQTT Broker!")
        else:
            print("Failed to connect, return code %d\n", rc)
    # Set Connecting Client ID
    client = mqtt_client.Client(client_id)
 
    client.on_connect = on_connect
    client.connect(broker, port)
    return client

def subscribe(client: mqtt_client):
    def on_message(client, userdata, msg):
        print(msg.payload.id)
        val = msg.payload.decode()
        print("val is " + str(val) )
        valin = val 
    
        swift.waiting_ready(timeout=20)
        device_info = swift.get_device_info()
        firmware_version = device_info['firmware_version']
        if firmware_version and not firmware_version.startswith(('0.', '1.', '2.', '3.')):
            swift.set_speed_factor(0.0005)
        
        print("send in direction")
        swift.set_mode(0)
        rotate = valin
        swift.set_polar(rotation = rotate , height= high , stretch=stret)        
        print("direction online")



    client.subscribe(topic)
    
    client.on_message = on_message
    
    

def run():
    client = connect_mqtt()
    subscribe(client)

   
    client.loop_forever()


if __name__ == '__main__':
    run()
