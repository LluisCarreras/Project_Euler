# -*- coding: utf-8 -*-
"""
Created on Thu Jan  7 22:50:46 2016

@author: Lluís


Special Pythagorean triplet
Problem 9

A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

a**2 + b**2 = c**2
For example, 3**2 + 4**2 = 9 + 16 = 25 = 5**2.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
"""


import math

def find_triplet():
    for a in range(1, 1000):
        for b in range(1, 1000):
            if a < b:
                duplet = a * a + b * b
                c = math.sqrt(duplet)
                c_floor = float(math.floor(c))
                if c == c_floor:
                    c = int(c)
                    sum_triplet = a + b + c
                    print(a, "\t", b, "\t", c, "\t", sum_triplet)
                    if sum_triplet == 1000:
                        return a, b, c

a, b, c = find_triplet() 
sum_triplet = a + b + c
prod_triplet = a * b * c                   
print(a, "\t", b, "\t", c, "\t", sum_triplet, "\t", prod_triplet)


            