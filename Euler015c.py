# -*- coding: utf-8 -*-
"""
Created on Thu Feb  4 16:43:36 2016
@author: Lluís Carreras González

Lattice paths
Problem 15

Starting in the top left corner of a 2×2 grid, and only being able to move 
to the right and down, there are exactly 6 routes to the bottom right corner.

How many such routes are there through a 20×20 grid?
"""

import time


def create_matrix(n):
    """
    Create the initial matrix nxn, with all the places with "1".
    """
    
    return [[1 for column in range(n)] for row in range(n)]
 
 
time_ini = time.time()  
   
matrix_order = 20
 
the_matrix = create_matrix(matrix_order + 1)
for row in range(1, matrix_order + 1):
    for col in range(1, matrix_order + 1):
        the_matrix[row][col] = the_matrix[row][col - 1] \
                + the_matrix[row - 1][col]

print("Result: \t", the_matrix[matrix_order][matrix_order])

time_end = time.time()
time_total = time_end - time_ini
print("Time required: \t", "{0:.6f}".format(time_total), "seconds") 
   
