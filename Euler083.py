# -*- coding: utf-8 -*-
"""
Created on Sun Dec 24 14:52:40 2017

@author: Lluís

Path sum: four ways
Problem 83 

NOTE: This problem is a significantly more challenging version of Problem 81.

In the 5 by 5 matrix below, the minimal path sum from the top left to the bottom right, by 
moving left, right, up, and down, is indicated in bold red and is equal to 2297.


Find the minimal path sum, in matrix.txt (right click and "Save Link/Target As..."), a 31K text 
file containing a 80 by 80 matrix, from the top left to the bottom right by moving left, right, 
up, and down.
"""


import numpy as np


def get_matrix(my_file):
    '''
    Return a list a lists, where every sublist is a row in the triangle.
    '''
    return [[int(num) for num in x.strip().split(",")] 
            for x in open(my_file, 'r').read().strip().split("\n")]


def get_min_path(the_matrix, initial_cell, final_cell):
    '''
    Finds the minimal path sum in matrix mat from the initial cell to the final cell.
    '''
    
    num_rows = len(the_matrix)
    num_cols = len(the_matrix[0])
    
    neighbors = {(row, col):[] for row in range(num_rows) for col in range(num_cols)}
    for cell in neighbors:
        if cell[0] > 0:
            neighbors[cell].append((cell[0] - 1, cell[1]))
        if cell[0] < num_rows - 1:
            neighbors[cell].append((cell[0] + 1, cell[1]))
        if cell[1] > 0:
            neighbors[cell].append((cell[0], cell[1] - 1))
        if cell[1] < num_cols - 1:
            neighbors[cell].append((cell[0], cell[1] + 1))
    
    vertexes = {(row, col):np.inf for row in range(num_rows) for col in range(num_cols)}
    distances = {(row, col):np.inf for row in range(num_rows) for col in range(num_cols)}
    previous_nodes = {(row, col):None for row in range(num_rows) for col in range(num_cols)}
    
    distances[initial_cell] = the_matrix[initial_cell[0]][initial_cell[1]]
    vertexes[initial_cell] = the_matrix[initial_cell[0]][initial_cell[1]]
    
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
                if final_cell == neighbor:
                    return distances[neighbor]
                    
    return "Not found"
        


#my_matrix = [[131, 673, 234, 103, 18],
#               [201, 96, 342, 965, 150],
#               [630, 803, 746, 422, 111],
#               [537, 699, 497, 121, 956],
#               [805, 732, 524, 37, 331],
#              ]


my_matrix = get_matrix('p083_matrix.txt')

num_rows = len(my_matrix)
num_cols = len(my_matrix[0]) 

minimum_paths = []
initial_cell = (0, 0)
final_cell = (num_rows - 1, num_cols - 1)

result = get_min_path(my_matrix, initial_cell, final_cell)  
print(result)

##################
# SOLUTION: 425185
##################