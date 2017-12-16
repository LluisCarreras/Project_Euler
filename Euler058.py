# -*- coding: utf-8 -*-
"""
Created on Sat Jan 30 16:10:38 2016

@author: Lluís Carreras González

Spiral primes
Problem 58

Starting with 1 and spiralling anticlockwise in the following way, a square 
spiral with side length 7 is formed.

    37 36 35 34 33 32 31
    38 17 16 15 14 13 30
    39 18  5  4  3 12 29
    40 19  6  1  2 11 28
    41 20  7  8  9 10 27
    42 21 22 23 24 25 26
    43 44 45 46 47 48 49

It is interesting to note that the odd squares lie along the bottom right 
diagonal, but what is more interesting is that 8 out of the 13 numbers lying 
along both diagonals are prime; that is, a ratio of 8/13 ≈ 62%.

If one complete new layer is wrapped around the spiral above, a square spiral 
with side length 9 will be formed. If this process is continued, what is the 
side length of the square spiral for which the ratio of primes along both 
diagonals first falls below 10%?
"""


import Euler_Project as ep


def spiral(n):
    """
    Return the terms of the four vertices in the n-th outer layer of a 
    (2n-1) by (2n-1) spiral.
    """
    
    dr = (2 * n - 1) * (2 * n - 1) # up-right term
    dl = dr - 2 * (n - 1)          # up-left term
    ul = dl - 2 * (n - 1)          # down-left term
    ur = ul - 2 * (n - 1)          # down-right term
    
    return ur, ul, dl, dr


def spiral_primes():
    """
    Solve the problem.
    """
    
    # Take into account the first caso, for layer 1.
    num_primes = 0
    num_total = 1
    ratio = 100.0
    
    # Start the iteration with layer 2
    layer = 2
    
    while ratio >= 10.0:
        side = 2 * layer - 1
        primes = sum([1 for i in spiral(layer) if ep.is_prime(i)])
        num_primes += primes
        num_total += 4
        ratio = 100.0 * num_primes / num_total
#        print(layer, "\t", side, "\t", ratio, "\t", num_primes, \
#                "\t", num_total)
        if ratio < 10.0:
            return layer, side
        layer += 1

print(spiral_primes())