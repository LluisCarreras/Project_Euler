# -*- coding: utf-8 -*-
"""
Created on Tue Jan 19 14:57:06 2016

@author: Lluís Carreras González

Sub-string divisibility
Problem 43

The number, 1406357289, is a 0 to 9 pandigital number because it is made up 
of each of the digits 0 to 9 in some order, but it also has a rather 
interesting sub-string divisibility property.

Let d1 be the 1st digit, d2 be the 2nd digit, and so on. In this way, we 
note the following:

d2d3d4=406 is divisible by 2
d3d4d5=063 is divisible by 3
d4d5d6=635 is divisible by 5
d5d6d7=357 is divisible by 7
d6d7d8=572 is divisible by 11
d7d8d9=728 is divisible by 13
d8d9d10=289 is divisible by 17
Find the sum of all 0 to 9 pandigital numbers with this property.
"""

        
def pandigitals(model, sub_list):
    """
    Create a list of pandigitals created with the digits in the model. The 
    starting sub_list is equal to the model.
    """
    
    if len(sub_list[0]) == len(model):
        return sub_list
    new_list = []
    for sl in sub_list:
        for m in model:
            if m not in sl:
                new_list.append(sl + m)
    return pandigitals(model, new_list)
        
        
def has_sub_string_divisibility(num):
    """
    Return True if the given number num has the property that the sub-strings
    are divisible by the consecutive primes.
    Return False otherwise.
    """
    
    num_str = str(num)
    if len(num_str) < 10:
        num_str = "0" + num_str
    divisors = [1, 2, 3, 5, 7, 11, 13, 17]
    
    for i in range(1, 8):
        if int(num_str[i:i+3]) % divisors[i] != 0:
            return False
    
    return True


def get_solution():   
    """
    Return a list with the pandigital numbers that have the property stated
    in this problem.
    """
     
    my_numbers = [] 
    expression = "0123456789" 
    pandigital_nums = pandigitals(list(expression), list(expression))     
    for pan in pandigital_nums:
        pan_int = int(pan)
        if has_sub_string_divisibility(pan_int):
            my_numbers.append(pan_int)
            print(pan_int)
    
    return my_numbers   
  
      
solution = get_solution()
print("Number of numbers in the solution:  ", len(solution))
print("Sum of the numbers in the solution: ", sum(solution))

