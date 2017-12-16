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

import Euler_Project as ep
from itertools import permutations
import math


def cube(num):
   """
   Return the cube of the given number num.
   """
   
   return int(math.pow(num, 3))


def cubic_permutations():
    my_cubes = {cube(n) for n in range(2, 3000)}
    #print(my_cubes[0])
    
    
    count = 0
    num_test = 345
    idx_cubes = 0
    
    
    while True:
        count = 0
        cube_test = cube(num_test)
#        my_str_list = [i for i in list(str(cube_test))]
#        print(my_str_list)
#        print(num_test, "\t", cube_test)
         
    #    permuts = []
    #    for i, n in enumerate(permutations(str(cube_test), len(str(cube_test)))):
    #        print(i, "\t", n)
    #        permuts.append(''.join(str(digit) for digit in n))
        
        permuts = set([int(''.join(permut)) for permut in 
                list(permutations(str(cube_test), len(str(cube_test))))])
                
#        for permut in permuts:
#            if permut in my_cubes:
#                count += 1
        primes = {i for i in permuts.intersection(my_cubes) if i >= cube_test}
        count = len(primes)
        print(num_test, "\t", count, "\t", primes)
        if count >= 5:
            return cube_test
        
#        if count >= 5:
#            return cube_test
        
#        print(num_test, "\t", cube_test, "\t", count)           
    #    print(permuts[:10])
    
        num_test += 1
    

print(cubic_permutations())










#my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
#my_str_list = [str(i) for i in my_list]
#
##print(permutations(my_str_list, my_str_list))
#
#result = permutations(my_str_list, my_str_list)[999999]
#print(result)