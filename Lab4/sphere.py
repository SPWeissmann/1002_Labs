#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 27 22:37:42 2019

@author: sam
"""
import math


def surface(radius):
    #surface area = 4 * pi * r^2
    return (4*math.pi*(radius**2))

def volume(radius):
    # volume = (4/3) * pi * r^3
    return (4*math.pi*(radius**3)) / 3
