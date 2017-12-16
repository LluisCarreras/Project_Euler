# -*- coding: utf-8 -*-
"""
Created on Sun Feb  7 00:50:39 2016

@author: Lluís Carreras González

Maximum path sum II
Problem 67

By starting at the top of the triangle below and moving to adjacent numbers 
on the row below, the maximum total from top to bottom is 23.

3
7 4
2 4 6
8 5 9 3

That is, 3 + 7 + 4 + 9 = 23.

Find the maximum total from top to bottom in triangle.txt (right click and 
'Save Link/Target As...'), a 15K text file containing a triangle with 
one-hundred rows.

NOTE: This is a much more difficult version of Problem 18. It is not possible 
to try every route to solve this problem, as there are 299 altogether! If you 
could check one trillion (1012) routes every second it would take over twenty 
billion years to check them all. There is an efficient algorithm to solve it. 
;o)
"""


import time


def get_triangle(my_file):
    """
    Return a list a lists, where every sublist is a row in the triangle.
    """
            
    return [[int(num) for num in x.strip().split(" ") ] 
            for x in open(my_file, 'r').read().strip().split("\n")]

    
# Set the initial time
time_ini = time.time() 
    
triangle = get_triangle('p067_triangle.txt') 
order = len(triangle)

# Beginning with the penultimate row upwards, fill the values in every row
# with the sum of the value itself plus the biggest of the the values 
# beneath.
for row in range(order - 2, -1, -1):
    for col in range(row + 1):
        triangle[row][col] += max(triangle[row + 1][col], 
                triangle[row + 1][col + 1])
 
# The maximum is the upper tip of the triangle       
maximum = triangle[0][0] 
print("\nMaximum total: ", maximum)

# Set the final time
time_end = time.time()
# Show the total required time.
time_total = time_end - time_ini
print("Required time: ", "{0:.4f}".format(time_total), "seconds") 