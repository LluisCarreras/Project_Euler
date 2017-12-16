# -*- coding: utf-8 -*-
"""
Created on Wed Jan 13 16:54:45 2016

@author: Lluís Carreras González

Lexicographic permutations
Problem 24

A permutation is an ordered arrangement of objects. For example, 3124 is one 
possible permutation of the digits 1, 2, 3 and 4. If all of the permutations 
are listed numerically or alphabetically, we call it lexicographic order. 
The lexicographic permutations of 0, 1 and 2 are:

012   021   102   120   201   210

What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 
5, 6, 7, 8 and 9?
"""

def permutations(digits, my_list):
    """
    Returns the list of permutations that can be made from the objects in
    the given list.
    """
    
    if len(my_list[0]) == len(digits) and len(my_list) > 0:
        return my_list
    else:
        new_list = []
        for item in my_list:
            for digit in digits:
                if digit not in item:
                    new_item = item + digit
                    new_list.append(new_item)
        return permutations(digits, new_list)
        
my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
my_str_list = [str(i) for i in my_list]

#print(permutations(my_str_list, my_str_list))

result = permutations(my_str_list, my_str_list)[999999]
print(result)
        