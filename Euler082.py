# -*- coding: utf-8 -*-
"""
Created on Tue Dec 19 20:52:33 2017

@author: Lluís

Path sum: three ways
Problem 82 
NOTE: This problem is a more challenging version of Problem 81.

The minimal path sum in the 5 by 5 matrix below, by starting in any cell in the left column 
and finishing in any cell in the right column, and only moving up, down, and right, is 
indicated in red and bold; the sum is equal to 994.

Find the minimal path sum, in matrix.txt (right click and "Save Link/Target As..."), a 31K 
text file containing a 80 by 80 matrix, from the left column to the right column.
"""

import numpy as np


def get_matrix(my_file):
    '''
    Return a list a lists, where every sublist is a row in the triangle.
    '''
    return [[int(num) for num in x.strip().split(",")] 
            for x in open(my_file, 'r').read().strip().split("\n")]


def get_min_path(the_matrix, source):
    '''
    Finds the minimal path sum in matrix mat from the source cell in the 
    leftest column to all the cells in the rightest column.
    '''
    
    num_rows = len(the_matrix)
    num_cols = len(the_matrix[0])
    
    neighbors = {(row, col):[] for row in range(num_rows) for col in range(num_cols)}
    for cell in neighbors:
        if cell[0] > 0:
            neighbors[cell].append((cell[0] - 1, cell[1]))
        if cell[0] < num_rows - 1:
            neighbors[cell].append((cell[0] + 1, cell[1]))
        if cell[1] < num_cols - 1:
            neighbors[cell].append((cell[0], cell[1] + 1))
    
    vertexes = {(row, col):np.inf for row in range(num_rows) for col in range(num_cols)}
    distances = {(row, col):np.inf for row in range(num_rows) for col in range(num_cols)}
    previous_nodes = {(row, col):None for row in range(num_rows) for col in range(num_cols)}
    
    distances[(source, 0)] = the_matrix[source][0]
    vertexes[(source, 0)] = the_matrix[source][0]
    
    while vertexes:
        min_value = min(vertexes.values())
        u = [k for k, v in vertexes.items() if distances[k] == min_value][0]
        vertexes.pop(u)
        
        for neighbor in neighbors[u]:
            if neighbor in vertexes:
                alt = distances[u] + the_matrix[neighbor[0]][neighbor[1]]
                if alt < distances[neighbor]:
                    distances[neighbor] = alt
                    vertexes[neighbor] = alt
                    previous_nodes[neighbor] = u
     
    return distances
    

#my_matrix = [[131, 673, 234, 103, 18],
#               [201, 96, 342, 965, 150],
#               [630, 803, 746, 422, 111],
#               [537, 699, 497, 121, 956],
#               [805, 732, 524, 37, 331],
#              ]


my_matrix = get_matrix('p082_matrix.txt')

num_rows = len(my_matrix)
num_cols = len(my_matrix[0]) 

minimum_paths = []
for round in range(num_rows):
    result = get_min_path(my_matrix, round)  
    minimum_path = min([v for k, v in result.items() if k[1] == num_cols - 1])  
    minimum_paths.append(minimum_path)
    print(round, minimum_path, min(minimum_paths))
    
print()
print(min(minimum_paths))


##################
# SOLUTION: 260324
##################

