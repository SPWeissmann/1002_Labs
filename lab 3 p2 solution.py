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
# Note to students: This is heavily over-commented and over-expanded code, 
# with the intention of explaining different aspects of the program. Please do 
# not take this as an example of what your comments or parenthese spacing
# should look like.
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

#by convention, ALL_CAPS variable names signal that the variable's values 
#should never be modified. However, Python does not enforce this and you
#could modify them if you wanted, it would just be bad practice. 
#
#Here we use them to make the code more understandable, e.g. by being able to 
#reference a direction as NORTH instead of 0.

X = 0 
Y = 1
NORTH = 0 
EAST = 1
SOUTH = 2
WEST = 3

random.seed() #re-seed our pseudo-random number generator (PRG) on start

#representing (x,y) coordinates as a list of two integers
starting_loc = [0,0] #save our starting location (used at end of program)
current_loc = [0,0] #we will use this variable seperately to track our current
                    #location, also starting from (0,0)

#each for-loop will make one move at random. We will make 100 moves in total.
for i in range(100):
    
    #random.random() generates a number between 0 and .9999...
    #multiplying it by 4 gives us a number from 0 to 3.999... 
    #converting it to an int rounds it down, so we get a number from 0-3
    direction = int( (random.random()*4) )

    #check which direction we need to go:
    if direction == NORTH: 
        #add 1 to the current x coordinate, and save it as the new x coordinate
        current_loc[1] = current_loc[X] + 1 
        
    elif direction == EAST:
        #add 1 to the current y coordinate, and save it as the new y coordinate
        current_loc[Y] = current_loc[Y] + 1
        
    elif direction == SOUTH:
        #subtract 1 from the current y coordinate, and save it as the new y coordinate
        current_loc[Y] = current_loc[Y] - 1
    
    elif direction == WEST:
        #subtract 1 from the current x coordinate, and save it as the new x coordinate
        current_loc[X] = current_loc[X] - 1
        
#calculate total distance moved:
x1 = starting_loc[X]
y1 = starting_loc[Y]        
        
x2 = current_loc[X]
y2 = current_loc[Y]

#abs() is a built in function that returns that absolute value of a number.
change_in_x = abs(x1-x2)
change_in_y = abs(y1-y2)

manhattan_dist = change_in_x + change_in_y
eucldn_dist = math.sqrt((change_in_x**2) + (change_in_y**2))

print("Manhattan distance is: ", manhattan_dist)
print("Euclidean distance is: ", round(eucldn_dist, 4))
#round(n, i) is a function that rounds a number, n, to i decimal places. 


