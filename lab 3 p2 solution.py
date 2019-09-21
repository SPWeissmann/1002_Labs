# -*- coding: utf-8 -*-
"""
Created on Thu Sep 19 10:11:42 2019

@author Samuel Weissmann
"""
import random
import math

# =============================================================================
# Note to students: This is heavily over-commented code, with the intention
# of explaining different aspects of the program. Please do not take this as 
# an example of what your comments should look like.
# =============================================================================

#ALL_CAPs marks that these are constant values, and should not be changed
X = 0
Y = 1
ORIGIN = [0,0]
NORTH = 0
EAST = 1
SOUTH = 2
WEST = 3

random.seed() #re-seed our pseudo-random number generator (PRG) on start
drunk_coords = ORIGIN #store the (x,y) coordinates as a list.

#each for-loop will make one move at random. We will make 100 moves in total.
for i in range(100):
    
    
#both lines generate a random integer between 0 and 3 in order to determine 
#which direction to take.
    direction = int((random.random() * 4)) #option 1
    #directions = random.randrange(4) #option 2

# =============================================================================
# Here we check which "direction" we have generated using the random function.
# 
# =============================================================================
    if direction == NORTH: 
       drunk_coords[1] = drunk_coords[X] + 1 
        
    #if the direction is east (aka 1), then add one to t   
    if direction == EAST:
        drunk_coords[Y] = drunk_coords[Y] + 1
        
    if direction == SOUTH:
        drunk_coords[Y] = drunk_coords[Y] - 1
    
    if direction == WEST:
        drunk_coords[X] = drunk_coords[X] - 1
        
#calculate distance from origin
x = drunk_coords[X]
y = drunk_coords[Y]

eucldn_dist = math.sqrt(x**2 + y**2)
manhattan_dist = abs(x) + abs(y)

print(manhattan_dist)

print( round(eucldn_dist, 4))


