#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 27 22:37:42 2019

@author: Samuel Weissmann
"""
import math


#The surface function accepts the sphere's radius 
#as an argument and returns the surface area of the sphere.
def surface(radius):
    #surface area = 4 * pi * r^2
    return (4*math.pi*(radius**2))

#The volume function accepts the sphere's radius as 
#an argument, and returns the volume of the sphere.
def volume(radius):
    # volume = (4/3) * pi * r^3
    return (4*math.pi*(radius**3)) / 3
