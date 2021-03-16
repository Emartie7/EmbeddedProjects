#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 14 20:03:52 2021

@author: emartie7
"""

from gpiozero import Robot
import time
myBuggy = Robot(left=(14,15),right=(7,8))

print("Starting pre-programmed motor sequence . . .")
myBuggy.forward(0.5)
time.sleep(3)
myBuggy.stop()
time.sleep(1)
myBuggy.backward(0.5)
time.sleep(3)
myBuggy.stop()

print("Initiating forward ramp")

for dc in range(0,10):
    print("Commanding duty cycle: {}".format(dc))
    myBuggy.forward(0.1*dc)
    time.sleep(1)
    
print("Completed motor exercise.")