# -*- coding: utf-8 -*-
"""
Created on Thu Sep 19 10:10:26 2019

@author: spw2136
"""
import random


# =============================================================================
# Part 1
# Goal: sum of all numbers from 1-100 (inclusive)
#
# The range() function generates a sequence of numbers. Range(101) will 
# generate a sequence of numbers from 0 to 100. Every time the for loop runs, 
# the variable i will take on the value of the next number in the sequence
# i.e. i will be 0, then 1, then 2, ... , then 100. 
#
# In the print statement, we convert the integer sum1 to a string using the 
# str() function. We then use string concatenation to combine both strings 
# in the print statement into one larger string to be printed.
# =============================================================================
sum1 = 0 #initialize our first sum value as zero

for i in range(101):
    sum = sum + i #add i to our sum each time the foor loop runs
    
print("sum of integers from 1-100 (inclusive) is: " + str(sum1))

# =============================================================================
# Part 2
# Goal: sum all even numbers from 1-100 (inclusive)
# 
# Here we will use a while loop. We control the loop with a "loop control
# variable" (LCV) i. The while loop will run as long as the 
# statement i < 101 is true. At the bottom of the while loop, we update
# our LCV by adding 1 to i everytime the while loop runs. Because i starts 
# at 0 and ends at 100, we know that the loop runs 101 times.
#  
# Doing i%2 gives us the remainder of dividing i by 2. If i is even, the the 
# remainder of dividing i by 2 should be 0. 
# =============================================================================
sum2 = 0 #initialize sum

i = 0 #initialize LCV
while i < 101:
    if i%2 == 0:
        sum2 = sum2 + i
    i = i + 1 #update our LCV

print("sum of all even integers from 1-100 (inclusive) is: " + str(sum2))

# =============================================================================
# part 3:
# sum of 100 random numbers from 1-10 (inclusive)
# =============================================================================
sum3 = 0

for i in range(100):
    rand_num = random.randrange(1,10)
    sum3 = sum3 + rand_num
    
print("sum of all even integers from 1-100 (inclusive) is: " + str(sum3))