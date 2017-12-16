# -*- coding: utf-8 -*-
"""
Created on Sun Jan 17 20:32:36 2016

@author: Lluís Carreras González

Circular primes
Problem 35

The number, 197, is called a circular prime because all rotations of the 
digits: 197, 971, and 719, are themselves prime.

There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 
71, 73, 79, and 97.

How many circular primes are there below one million?
"""

import math


def is_prime(num):
    """
    Evaluate wether the given number num is prime.
    """
    
    if num > 2:
        for i in range(2, int(math.sqrt(num)) + 1):
            if num % i == 0:
                return False
    return True
    
    
def is_circular(num):
    """
    Evaluate wether the given number num is circular.
    """
    
#    print(num)
    if not is_prime(num):
        return False
    duplicate = 2 * str(num)
#    rotations = [int(duplicate[i:i + len(str(num))]) 
#            for i in range(len(str(num)))] 
    for i in range(len(str(num))):
        rotation = int(duplicate[i:i + len(str(num))])
        if not is_prime(rotation):
            return False
    return True
 
   
for num in [100, 1000000]:
    circulars = [n for n in range(2, num) if is_circular(n)]
    print(circulars)
    print(len(circulars))
    print("\n")
        
 