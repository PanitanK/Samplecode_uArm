from multiprocessing.connection import wait
import os
from pickle import TRUE
from re import X

import sys
import time
import functools
import keyboard
sys.path.append(os.path.join(os.path.dirname(__file__), '../../..'))
from uarm.wrapper import SwiftAPI
swift = SwiftAPI(filters={'hwid': 'USB VID:PID=2341:0042'})
from uarm.swift.protocol import SERVO_BOTTOM, SERVO_LEFT, SERVO_RIGHT, SERVO_HAND

# Function declaration 


# I ll let you input a value (1-5) to see the 5 possible actions then you can change by getting it 
#  from your model either it's a prediction or whatever just get an output as int from 1-5 will be fine

# Please place an uArm at the edge of a table because some of it will move a tip below a base 



swift.waiting_ready(timeout=20)
device_info = swift.get_device_info()
firmware_version = device_info['firmware_version']
if firmware_version and not firmware_version.startswith(('0.', '1.', '2.', '3.')):
    swift.set_speed_factor(0.0005)
swift.set_mode(0)
swift.set_polar()





while(True):

    swift.waiting_ready(timeout=20)
    device_info = swift.get_device_info()
    firmware_version = device_info['firmware_version']
    if firmware_version and not firmware_version.startswith(('0.', '1.', '2.', '3.')):
        swift.set_speed_factor(0.0005)
    swift.set_mode(0)
    swift.set_polar()

    print("\n\n\n\n\n")
    in_put = input("Type 1-5 : ")
    print("Aciton : " + in_put)
    


# Pick up a coin 1

    if in_put == "1" :
        swift.waiting_ready(timeout=20)
        device_info = swift.get_device_info()
        firmware_version = device_info['firmware_version']
        if firmware_version and not firmware_version.startswith(('0.', '1.', '2.', '3.')):
            swift.set_speed_factor(1)
        swift.set_polar( stretch= 300 , rotation = 10    , height= 0 )
        swift.set_pump(on=True)
        swift.set_polar( stretch= 300 , rotation = 10    , height= 100 )
        swift.set_polar( stretch= 300 , rotation = 170    , height= 100 )
        swift.set_polar( stretch= 300 , rotation = 170    , height= 0 )
        swift.set_pump(on=False)
        swift.set_polar( stretch= 300 , rotation = 90    , height= 150 )



    # Pick up a coin 2

    if in_put == "2" :
        swift.waiting_ready(timeout=20)
        device_info = swift.get_device_info()
        firmware_version = device_info['firmware_version']
        if firmware_version and not firmware_version.startswith(('0.', '1.', '2.', '3.')):
             swift.set_speed_factor(0.02)
        swift.set_polar( stretch= 300 , rotation = 170    , height= 0 )
        swift.set_pump(on=True)
        swift.set_polar( stretch= 300 , rotation = 170    , height= 100 )
        swift.set_polar( stretch= 300 , rotation = 10    , height= 100 )
        swift.set_polar( stretch= 300 , rotation = 10    , height= 0 )
        swift.set_pump(on=False)
        swift.set_polar( stretch= 200 , rotation = 90    , height= 150 )
        
    
    
    
    
    # Dump a paper
    
    if in_put == "3" :
        swift.waiting_ready(timeout=20)
        device_info = swift.get_device_info()
        firmware_version = device_info['firmware_version']
        if firmware_version and not firmware_version.startswith(('0.', '1.', '2.', '3.')):
            swift.set_speed_factor(0.02)
        swift.set_polar( stretch= 150 , rotation = 90    , height= 0 )
        time.sleep(2)
        swift.set_pump(on=True)
        swift.set_polar( stretch= 220 , rotation = 90    , height= 0 )
        time.sleep(2)
        swift.set_polar( stretch= 300 , rotation = 90    , height= 150 )
        swift.set_polar( stretch= 350 , rotation = 90    , height= 150 )
        swift.set_pump(on=False)




    #Draw 2 squares ( If you have a gripper )

    if in_put == "4" :
        swift.waiting_ready(timeout=20)
        device_info = swift.get_device_info()
        firmware_version = device_info['firmware_version']
        if firmware_version and not firmware_version.startswith(('0.', '1.', '2.', '3.')):
             swift.set_speed_factor(0.02)
        swift.set_position(x = 100 ,y = 100 , z =  100 )
        swift.set_position(x = 200 ,y = 100 , z =  100 )
        swift.set_position(x = 200 ,y = 200 , z =  100 )
        swift.set_position(x = 100 ,y = 200 , z =  100 )
        swift.set_position(x = 100 ,y = 100 , z =  100 )

        swift.set_position(x = 100 ,y = -100 , z =  100 )
        swift.set_position(x = 200 ,y = -100 , z =  100 )
        swift.set_position(x = 200 ,y = -200 , z =  100 )
        swift.set_position(x = 100 ,y = -200 , z =  100 )
        swift.set_position(x = 100 ,y = -100 , z =  100 )
    


     #Draw a parallelogram ( If you have a gripper )

    if in_put == "5" :
        swift.waiting_ready(timeout=20)
        device_info = swift.get_device_info()
        firmware_version = device_info['firmware_version']
        if firmware_version and not firmware_version.startswith(('0.', '1.', '2.', '3.')):
             swift.set_speed_factor(0.02)
        swift.set_position(x = 200 ,y = 0 , z =  0 )

        swift.set_position(x = 250 ,y = 100 , z =  0 )

        swift.set_position(x = 300 ,y = 0 , z =  0 )

        swift.set_position(x = 250 ,y = -100 , z =  0 )
      
        swift.set_position(x = 200 ,y = 0 , z =  0 )



    if in_put == "6" :
        
        swift.set_position(x = 100 ,y = 200 , z = 0 )
        
        swift.waiting_ready(timeout=20)
        device_info = swift.get_device_info()
        firmware_version = device_info['firmware_version']
        if firmware_version and not firmware_version.startswith(('0.', '1.', '2.', '3.')):
             swift.set_speed_factor(0.02)
        swift.set_position(x = 280 ,y = 200 , z =  0 )
        swift.set_position(x = 280 ,y = -200 , z =  0 )
        swift.set_position(x = 100 ,y = -200 , z =  0 )
        print("Exiting")
        
    if in_put == "7" :
        
        swift.set_position(x = 200 ,y = 0, z = 100 )
        
        swift.waiting_ready(timeout=20)
        device_info = swift.get_device_info()
        firmware_version = device_info['firmware_version']
        if firmware_version and not firmware_version.startswith(('0.', '1.', '2.', '3.')):
             swift.set_speed_factor(0.02)
        swift.set_position(x = 200 ,y = 0 , z =  -8 )
        swift.set_pump(on=True)
        swift.set_position(x = 200 ,y = 0 , z =  130 )
        swift.set_position(x = 250 ,y = 100 , z =  130 )
        swift.set_position(x = 250 ,y = 100 , z =  100 )
        swift.set_pump(on=False)
        print("Exiting")
    
    if in_put == "7" :
        
        swift.set_position(x = 200 ,y = 0, z = 100 )
        
        swift.waiting_ready(timeout=20)
        device_info = swift.get_device_info()
        firmware_version = device_info['firmware_version']
        if firmware_version and not firmware_version.startswith(('0.', '1.', '2.', '3.')):
             swift.set_speed_factor(0.02)
        pocor = swift.get_polar()
        print("\n")
        print(" Coordinate in polar = : " )
        print(pocor)
        stret = pocor[0]
        rotate = pocor[1]
        high = pocor[2]
        print("Exiting")
