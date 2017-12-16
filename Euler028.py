# -*- coding: utf-8 -*-
"""
Created on Wed Jan 13 20:12:01 2016

@author: Lluís Carreras González

Number spiral diagonals
Problem 28

Starting with the number 1 and moving to the right in a clockwise direction 
a 5 by 5 spiral is formed as follows:

        21 22 23 24 25
        20  7  8  9 10
        19  6  1  2 11
        18  5  4  3 12
        17 16 15 14 13

It can be verified that the sum of the numbers on the diagonals is 101.

What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral 
formed in the same way?
"""


def spiral(n):
    """
    Returns the sum of the numbers on the diagonals in a n by n spiral.
    """
    
    total = 1
    for n in range(3, spiral_range + 1, 2):
        # Every turn in the spiral adds four terms.
        ur = n * n                      # up-right term
        ul = n * n - n + 1              # up-left term
        dl = n * n - 2 * n + 2          # down-left term
        dr = n * n - 3 * n + 3          # down-right term
        subtotal = ur + ul + dl + dr
        total += subtotal
    return total


spiral_range = 1001
print(spiral(spiral_range))