# -*- coding: utf-8 -*-
"""
Created on Tue Dec 19 12:03:15 2017

@author: jlcarreras

Path sum: two ways
Problem 81 

In the 5 by 5 matrix below, the minimal path sum from the top left to the 
bottom right, by only moving to the right and down, is indicated in bold red 
and is equal to 2427.

Find the minimal path sum, in matrix.txt (right click and "Save Link/Target 
As..."), a 31K text file containing a 80 by 80 matrix, from the top left 
to the bottom right by only moving right and down.

"""


import numpy as np


def get_matrix(my_file):
    '''
    Return a list a lists, where every sublist is a row in the triangle.
    '''
    return [[int(num) for num in x.strip().split(",")] 
            for x in open(my_file, 'r').read().strip().split("\n")]


def get_min_path(mat):
    '''
    Finds the minimal path sum, in matrix mat from the top left 
    to the bottom right by only moving right and down.
    '''
    
    num_rows = len(mat)
    num_cols = len(mat[0])
    
    dummy_mat = np.zeros(shape=(num_rows, num_cols))
    
    # Populate the last place in the dummy matrix
    dummy_mat[num_rows-1][num_cols-1] = mat[num_rows-1][num_cols-1]
    
    # Populate the last column
    for row in range(num_rows-2, -1, -1):
        dummy_mat[row][num_cols - 1] = mat[row][num_cols - 1] + dummy_mat[row + 1][num_cols - 1]
        
    # Populate the last row
    for col in range(num_cols-2, -1, -1):
        dummy_mat[num_rows - 1][col] = mat[num_rows - 1][col] + dummy_mat[num_rows - 1][col + 1]
    
    # Populate the rest of places
    for col in range(num_cols - 2, -1, -1):
        for row in range(num_rows -2, -1, -1):
           dummy_mat[row][col] = mat[row][col] + min(dummy_mat[row + 1][col], dummy_mat[row][col + 1]) 
    
#    print(dummy_mat)
    
    # Seek the minimum path
    path = [mat[0][0]]
    idx_row = 0
    idx_col = 0
    while idx_row < num_rows - 1 and idx_col < num_cols - 1:
#        if idx_row == num_rows - 1 and idx_col == num_cols - 1:
#            pass
        if idx_row == num_rows - 1:
            idx_col += 1
        elif idx_col == num_cols - 1:
            idx_row += 1
        elif dummy_mat[idx_row + 1][idx_col] < dummy_mat[idx_row][idx_col + 1]:
            idx_row += 1
        else:
            idx_col += 1
        path.append(mat[idx_row][idx_col])
    path.append(mat[num_rows - 1][num_cols - 1])
    
    return path


#test_matrix = [[4,5,8],
#               [9,1,3],
#               [2,6,7]]


my_matrix = get_matrix('p081_matrix.txt')
result = get_min_path(my_matrix)    
print(result)
print(sum(result))