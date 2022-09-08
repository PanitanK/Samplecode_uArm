from ast import While
from cmath import cos, pi

import numpy as np
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
UAL = 158.8
LAL = 142

def spin() : 
     
     swift.waiting_ready(timeout=20)
     device_info = swift.get_device_info()
     firmware_version = device_info['firmware_version']
     if firmware_version and not firmware_version.startswith(('0.', '1.', '2.', '3.')):
          swift.set_speed_factor(0.02)
     swift.set_position(x = x ,y = y, z = z )
          
     
     return()

while a != "esc":
   
     print("Input variables")
     Base , LA ,UA = float(input("Base Angle : ")) , float(input("Lower Arm Angle : ")) , float(input("Upper Arm Angle : "))
     eps = np.radians(Base-90)
     cos_e = float(np.cos(eps))
     sin_e = float(np.sin(eps))
     RT = np.array((
         ( cos_e      ,sin_e*-1        , 0 ),
         ( sin_e      ,cos_e           , 0 ),
         (0           ,0               , 1 )
     ))
     #print(RT)
     UALX = LAL*(float(np.cos(np.radians(LA)))) + UAL*(float(np.cos(np.radians(UA*-1)))) + 69.91
     LALX = LAL*(float(np.sin(np.radians(LA)))) + UAL*(float(np.sin(np.radians(UA*-1)))) + 32.26
     V = np.array( ( [UALX],[0],[LALX] ) )
     #print(V)
     Vec = np.dot(RT,V)
     #print(str(Vec[0]) + str(Vec[1]) + str(Vec[2]))
     x = str(round(Vec[0][0] , 2 ))
     y = str(round(Vec[1][0] , 2 ))
     z = str(round(Vec[2][0] , 2 ))
     print("X = : " + x + " Y = : " + y + " Z = : " + z)
     spin()
     
     del Base , LA ,UA
     print("Moving")
     a = keyboard.read_key()
     input("Press anything to resume , ESC + Enter to quit ")

