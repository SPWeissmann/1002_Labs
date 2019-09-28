#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 27 22:37:51 2019

@author: sam
"""
import circle


def surface(height, radius):
    #surface area  = (2 * pi * radius * height) + (2 * pi * r^2)
    #              = (base circumference * height) + (2 * base area)
    #              = area of sides + area of two ends
    ends_area =  2 * circle.area(radius)
    sides_area = circle.circumference(radius) * height
    return ends_area + sides_area

def volume(height, radius):
    #volume = base * height
    base = circle.area(radius)
    return base * height