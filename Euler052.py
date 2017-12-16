# -*- coding: utf-8 -*-
"""
Created on Sat Jan 30 13:06:44 2016

@author: Lluís Carreras González

Permuted multiples
Problem 52

Published on Friday, 12th September 2003, 06:00 pm; Solved by 43361; 
Difficulty rating: 5%

It can be seen that the number, 125874, and its double, 251748, contain 
exactly the same digits, but in a different order.

Find the smallest positive integer, x, such that 2x, 3x, 4x, 5x, and 6x, 
contain the same digits.
"""


def permuted_multiples(max_mult):
    """
    Return the smallest positive integer x such that its multiples up to the
    maximum multiple max_mult contain the same digits than such integer.
    """
    
    num_test = 1  
    count = 1
    
    while count < max_mult:
        num_list = sorted([n for n in str(num_test)])
        count = 1
        for mult in range(2, max_mult + 1):
            if sorted(list(str(mult * num_test))) == num_list:
                count += 1
            else:
                break
            if count == max_mult:
                return num_test
        num_test += 1       
 
   
print("Case 2: ", permuted_multiples(2))            
print("Case 6: ", permuted_multiples(6))