# -*- coding: utf-8 -*-
"""
Created on Thu Sep 19 10:11:42 2019

@author Samuel Weissmann

This program simulates a person walking around Manhattan from intersection 
to intersection. At each intersection, they choose a new direction at random 
and walk one block. After 100 such choices, we want to know how far away they
are from their starting position, both in "Manhattan Distance", and shortest
path / straight line distance (Euclidean distance).
"""
# =============================================================================
# Note to students: This is heavily over-commented code, with the intention
# of explaining different aspects of the program. Please do not take this as 
# an example of what your comments should look like.
#
#
# In order to track the person's movements and location, we imagine that the 
# grid of blocks is a cartesian plane (a 2D-plane with an x and y axis), and 
# we store the person's current location as a pair of x,y coordinates on 
# this plane. We interpret moving north-south as moving along the y-axis, and 
# moving east-west as moving along the x-axis. 
#
# The coordinates are stored as a list of two integers, where the first 
# integer is the value of the x coordinate, and the second integer is the 
# value of the y coordinate.
#
#
# This program does 3 things:
# 
# 1. Getting ready: We import the modules we will need to use (math and random)
#    and we define our constant values using ALL_CAPS to indicate that they
#    should not be changed. We then generate a new need for our pseudo-random
#    number generator, and initialize our starting coordinates to the (0,0)
#
# 2. Movement: Using the random module's pseudo-random number generator (PRG), 
#    we generate an integer between 0 and 3 (inclusive) where 0 corresponds to
#    north, 1 corresponds to east, 2 corresponds to south, and 3 corresponds to
#    west. We check which direction we generated using if and elif statements,
#    and then add or subtract 1 from the appropriate coordinate to update our 
#    person's location.
#
# 3. Calculate distance: We want to print to the user how far the the person
#    walked from their original starting position, both in terms of total 
#    blocks walked, and in terms of straight line distance (i.e. shortest 
#    direct path). 
#    
#    The forumla for "Manhattan distance" is simply total vertical distance +
#    total horizontal distance (i.e. change in x + change in y). The 
#    Euclidean distance is found by:
#           squareroot( (x1-x2)^2 + (y1-y2)^2 )
#    where (x1,y1) are the starting coordinates, and (x2,y2) are 
#    the coordinates of our person's current location.
# =============================================================================

import random
import math


X = 0 
Y = 1
ORIGIN = [0,0] #representing (x,y) coordinates (0,0) as a list of two ints
NORTH = 0 
EAST = 1
SOUTH = 2
WEST = 3

random.seed() #re-seed our pseudo-random number generator (PRG) on start
starting_loc_coords = [0,0]
loc_coords = ORIGIN #initialize our starting coordinates to (0,0)

#each for-loop will make one move at random. We will make 100 moves in total.
for i in range(100):
    
    
    #both lines generate a random integer between 0 and 3
    direction = int((random.random() * 4))
    #directions = random.randrange(4) 

    #check which direction we need to go:
    
    if direction == NORTH: 
        #add 1 to the current x coordinate, and save it as the new x coordinate
        loc_coords[1] = loc_coords[X] + 1 
        
    elif direction == EAST:
        #add 1 to the current y coordinate, and save it as the new y coordinate
        loc_coords[Y] = loc_coords[Y] + 1
        
    elif direction == SOUTH:
        #subtract 1 from the current y coordinate, and save it as the new y coordinate
        loc_coords[Y] = loc_coords[Y] - 1
    
    elif direction == WEST:
        #subtract 1 from the current x coordinate, and save it as the new x coordinate
        loc_coords[X] = loc_coords[X] - 1
        
#calculate distance from origin
x1 = ORIGIN[X]
y1 = ORIGIN[Y]        
        
x2 = loc_coords[X]
y2 = loc_coords[Y]

print(  ORIGIN)

change_in_x = abs(x1-x2)
change_in_y = abs(y1-y2)

manhattan_dist = change_in_x + change_in_y

eucldn_dist = math.sqrt((change_in_x**2) + (change_in_y**2))

print("Manhattan distance is: ", manhattan_dist)
print( round(eucldn_dist, 4))


