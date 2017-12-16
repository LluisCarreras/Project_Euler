# -*- coding: utf-8 -*-
"""
Created on Sun Jan 31 18:25:58 2016

@author: Lluís Carreras González


Cubic permutations
Problem 62

The cube, 41063625 (345**3), can be permuted to produce two other cubes: 
56623104 (384**3) and 66430125 (405**3). In fact, 41063625 is the smallest cube 
which has exactly three permutations of its digits which are also cube.

Find the smallest cube for which exactly five permutations of its digits 
are cube.
"""


import math
import time


def cube(num):
   """
   Return the cube of the given number num.
   """
   
   return int(math.pow(num, 3))


time_ini = time.time()

num_test = 300
num_dict ={}

while True:
    num_cube = cube(num_test)
    num_sorted = ''.join(sorted(str(num_cube)))
    if num_sorted in num_dict:
        num_dict[num_sorted].append(num_test)
        if len(num_dict[num_sorted]) >= 5:
            print("Smallest number: \t", min(num_dict[num_sorted]))
            print("Its cube: \t\t", cube(min(num_dict[num_sorted])))
            break
    else:
        num_dict[num_sorted] = [num_test]
    num_test += 1

time_end = time.time()
time_total = time_end - time_ini
print("Time required: \t", "{0:.3f}".format(time_total), "seconds")  

