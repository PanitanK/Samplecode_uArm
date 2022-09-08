
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





print("Reset to default position")
#swift.set_servo_angle(servo_id=3, angle=30)
#swift.set_servo_angle(servo_id=2, angle=30)
#swift.set_servo_angle(servo_id=1, angle=30)


#swift.set_servo_angle(servo_id=1, angle = 60 )
#swift.set_servo_angle(servo_id=2, angle = 30 )
swift.set_position(x = 200 ,y = 0, z = 100 )

ANG0 = swift.get_servo_angle( servo_id=0 )
ANG1 = swift.get_servo_angle( servo_id=1 )
ANG2 = swift.get_servo_angle( servo_id=2 )
print( "servo ID0 is : " + str(swift.get_servo_angle( servo_id=0 )) +"\nservo ID1 is : "+ str( swift.get_servo_angle( servo_id=1 ) ) +"\nservo ID2 is : "+ str (swift.get_servo_angle( servo_id=2 )) +"\nAll Servo are : "+ str (swift.get_servo_angle( servo_id=3 )) )
while a != "esc":
        a = keyboard.read_key()
        print(a)
        print("Is ready")
        if a == "5" :
        
            swift.waiting_ready(timeout=20)
            device_info = swift.get_device_info()
            firmware_version = device_info['firmware_version']
            if firmware_version and not firmware_version.startswith(('0.', '1.', '2.', '3.')):
                swift.set_speed_factor(0.0005)
            print(a)
            print( "The position is " )
            print( swift.get_position() )
            print( "The servoangle is " )
            print( swift.get_servo_angle() )
        
        if a == "up" :
        
            print( swift.get_servo_angle() )
            print( "moving ANG0 + 5")
            ANG0 = ANG0 + 1
            swift.set_servo_angle(servo_id=0, angle = ANG0)

        if a == "down" :
        
            print( swift.get_servo_angle() )
            print( "moving ANG0 - 5")
            ANG0 = ANG0 - 1
            swift.set_servo_angle(servo_id=0, angle = ANG0)

        if a == "+" :
        
            print( swift.get_servo_angle() )
            print( "moving ANG1 + 5")
            ANG1 = ANG1 + 1
            swift.set_servo_angle(servo_id=1, angle = ANG1)

        if a == "-" :
        
            print( swift.get_servo_angle() )
            print( "moving ANG1 - 5")
            ANG1 = ANG1 - 1
            swift.set_servo_angle(servo_id=1, angle = ANG1)

        if a == "w" :
        
            print( swift.get_servo_angle() )
            print( "moving ANG2 + 5")
            ANG2 = ANG2 + 1
            swift.set_servo_angle(servo_id=2, angle = ANG2)

        if a == "s" :
        
            print( swift.get_servo_angle() )
            print( "moving ANG2 - 5")
            ANG2 = ANG2 - 1
            swift.set_servo_angle(servo_id=2, angle = ANG2)

    
print("Is Disconnected")   


        
