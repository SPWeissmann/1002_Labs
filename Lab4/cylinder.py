#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 27 22:37:51 2019

@author: Samuel Weissmann
"""
import circle


#The surface function accepts the sphere's height and radius 
#as arguments, and returns the surface area of the cylinder
def surface(height, radius):
    #surface area  = (2 * pi * radius * height) + (2 * pi * r^2)
    #              = (base circumference * height) + (2 * base area)
    #              = area of sides + area of two ends
    ends_area =  2 * circle.area(radius)
    sides_area = circle.circumference(radius) * height
    return ends_area + sides_area

#The volume function accepts the cylinder's height and radius as 
#as arguments, and returns the volume of the cylinder
def volume(height, radius):
    #volume = base * height
    base = circle.area(radius)
    return base * height