
from multiprocessing.connection import wait
import os
from re import X

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
i = 1
j = 1

swift.waiting_ready(timeout=20)
device_info = swift.get_device_info()
firmware_version = device_info['firmware_version']
if firmware_version and not firmware_version.startswith(('0.', '1.', '2.', '3.')):
    swift.set_speed_factor(0.0005)
swift.set_mode(0)
swift.set_polar()




print("Reset to default position")


while a != "esc":
        a = keyboard.read_key()
        print(a)
        print("Is ready")
        if a == "left" :
        
            swift.waiting_ready(timeout=20)
            device_info = swift.get_device_info()
            firmware_version = device_info['firmware_version']
            if firmware_version and not firmware_version.startswith(('0.', '1.', '2.', '3.')):
                swift.set_speed_factor(0.0005)
            print(a)
            print("send in direction")
            swift.set_mode(0)
            rotate = rotate + 5
            swift.set_polar(rotation = rotate , height= high , stretch=stret)
            
            print("direction online")
    
        elif a == "right" :
        
            swift.waiting_ready(timeout=20)
            device_info = swift.get_device_info()
            firmware_version = device_info['firmware_version']
            if firmware_version and not firmware_version.startswith(('0.', '1.', '2.', '3.')):
                swift.set_speed_factor(0.0005)
            print(a)
            print("send in direction")
            swift.set_mode(0)
            rotate = rotate - 5
            swift.set_polar(rotation = rotate , height= high , stretch=stret)
            
            print("direction online")

        elif a == "up" :
            swift.waiting_ready(timeout=20)
            device_info = swift.get_device_info()
            firmware_version = device_info['firmware_version']
            if firmware_version and not firmware_version.startswith(('0.', '1.', '2.', '3.')):
                swift.set_speed_factor(0.0005)
            print(a)
            print("send in direction")
            swift.set_mode(0)
            high = high + 5
            swift.set_polar(rotation = rotate , height= high , stretch=stret)
            print("direction online")


        elif a == "down" :
            swift.waiting_ready(timeout=20)
            device_info = swift.get_device_info()
            firmware_version = device_info['firmware_version']
            if firmware_version and not firmware_version.startswith(('0.', '1.', '2.', '3.')):
                swift.set_speed_factor(0.0005)
            print(a)
            print("send in direction")
            swift.set_mode(0)
            high = high - 5
            swift.set_polar(rotation = rotate , height= high , stretch=stret)
            
            print("direction online")

        elif a == "r" :
        
            swift.waiting_ready(timeout=20)
            device_info = swift.get_device_info()
            firmware_version = device_info['firmware_version']
            if firmware_version and not firmware_version.startswith(('0.', '1.', '2.', '3.')):
                swift.set_speed_factor(0.0005)
            print(a)
            print("send in direction")
            swift.set_mode(0)
         
            swift.set_polar(stretch=200 ,rotation=90 ,height=150)
            rotate = 90
            stret = 200
            high = 150
            print("default")


        elif a == "esc" :
            swift.disconnect()

        elif a == "+" :
            swift.waiting_ready(timeout=20)
            device_info = swift.get_device_info()
            firmware_version = device_info['firmware_version']
            if firmware_version and not firmware_version.startswith(('0.', '1.', '2.', '3.')):
                swift.set_speed_factor(0.0005)
            print(a)
            print("send in direction")
            swift.set_mode(0)
            stret = stret + 5
            swift.set_polar(rotation = rotate , height= high , stretch=stret)
            
            print("direction online")
        
        elif a == "-" :
            swift.waiting_ready(timeout=20)
            device_info = swift.get_device_info()
            firmware_version = device_info['firmware_version']
            if firmware_version and not firmware_version.startswith(('0.', '1.', '2.', '3.')):
                swift.set_speed_factor(0.0005)
            print(a)
            print("send in direction")
            swift.set_mode(0)
            stret = stret - 5
            swift.set_polar(rotation = rotate , height= high , stretch=stret)
            
            print("direction online")
        
        elif a == "5" :
            swift.waiting_ready(timeout=20)
            device_info = swift.get_device_info()
            firmware_version = device_info['firmware_version']
            if firmware_version and not firmware_version.startswith(('0.', '1.', '2.', '3.')):
                swift.set_speed_factor(0.0005)
            print(a)
            print("send in direction")
            swift.set_mode(0)
            stret = stret - 5
            pocor = swift.get_polar()
            axcor = swift.get_position()
            print(" Coordinate in polar = : ")
            print(pocor)
            print("\n")
            print(" Coordinate in axial = : " )
            print(axcor)
            print("\n")
            
            print("direction online")

        elif a == "d" :
            i = i % 2
            if i == 1 :
                print(swift.set_servo_detach())
            
            else :
                print(swift.set_servo_attach())
            i = i+1
            time.sleep(2)

        elif a == "ctrl" :
            print("set")
            swift.waiting_ready(timeout=20)
            device_info = swift.get_device_info()
            firmware_version = device_info['firmware_version']
            if firmware_version and not firmware_version.startswith(('0.', '1.', '2.', '3.')):
                swift.set_speed_factor(0.0005)
         
            print("send in direction")
            swift.set_mode(0)
         
            pocor = swift.get_polar()
    
            print("\n")
            print(" Coordinate in polar = : " )
            print(pocor)
            stret = pocor[0]
            rotate = pocor[1]
            high = pocor[2]
            
            swift.set_polar(rotation = rotate , height = high , stretch = stret)
            print("\n")
            print("direction online")
        
        elif a == "space" :
            print("set")
            swift.waiting_ready(timeout=20)
            device_info = swift.get_device_info()
            firmware_version = device_info['firmware_version']
            if firmware_version and not firmware_version.startswith(('0.', '1.', '2.', '3.')):
                swift.set_speed_factor(0.0005)
         
            print("send in direction")
            swift.set_mode(3)

            j = j % 2
            if j == 1 :
                swift.set_pump(on=True)
                print("pump on")
            else :
                swift.set_pump(on=False)
                print("pump off")
            j = j+1
            time.sleep(2)
         
            
     
        
        
      
            
         