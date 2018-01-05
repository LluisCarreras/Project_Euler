# -*- coding: utf-8 -*-
"""
Created on Wed Jan 13 16:06:27 2016
@author: Lluís Carreras González

Non-abundant sums
Problem 23

A perfect number is a number for which the sum of its proper divisors is 
exactly equal to the number. For example, the sum of the proper divisors of 
28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.

A number n is called deficient if the sum of its proper divisors is less 
than n and it is called abundant if this sum exceeds n.

As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest 
number that can be written as the sum of two abundant numbers is 24. By 
mathematical analysis, it can be shown that all integers greater than 28123 
can be written as the sum of two abundant numbers. However, this upper limit 
cannot be reduced any further by analysis even though it is known that the 
greatest number that cannot be expressed as the sum of two abundant numbers 
is less than this limit.

Find the sum of all the positive integers which cannot be written as the 
sum of two abundant numbers.
"""

import math

def search_divisors(number):
    """ 
    Calculates the proper divisors of a given number. The number is 
    not included in the returned list.
    """
    
    divisors = [1]
    for i in range(2, int(math.sqrt(number)) + 1):
        if number % i == 0:
            divisors.append(i)
            divisors.append(round(number / i))
    return sorted(divisors)
    
    
def is_abundant(n):
    """
    Returns a boolean that states wether the given number is abundant.
    """
    
    return sum(set(search_divisors(n))) > n


def abundants(n):
    """
    Returns a list containing all the abundant numbers up to the given number.
    """
    
    return [i for i in range(1, n + 1) if is_abundant(i)]
 
   
def sum_of_pairs(my_list):
    """
    Returns a list with all the possible sums of two numbers taken from
    the given list.
    """
    
    return sorted(list(set([n + m for n in my_list for m in my_list])))
    
    
def total_sum():
    """
    Returns the sum of all the positive integers which cannot be written as
    the sum of two abundant numbers
    """
    
    total = 0
    limit = 28123
    sums_of_pairs = sum_of_pairs(abundants(28123))
    for n in range(limit + 1):
        if n not in sums_of_pairs:
            total += n
    return total
    
    
#print(abundants(100))
#print(sum_of_pairs(abundants(100)))
    
print(total_sum())
    
    
