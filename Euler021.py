# -*- coding: utf-8 -*-
"""
Created on Wed Jan 13 13:19:48 2016
@author: Lluís Carreras González

Amicable numbers
Problem 21

Let d(n) be defined as the sum of proper divisors of n (numbers less than n
 which divide evenly into n).
 
If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair 
and each of a and b are called amicable numbers.

For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 
55 and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 
and 142; so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10000.
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
    

def d_function(number):
    """
    Returns the sum of the divisors of the given number.
    """
    return sum(search_divisors(number))


def search_amicable_numbers(number):
    """
    Returns a dict whose keys are the d(n) values for the numbers until a 
    given number and the values are lists with the numbers whose d(n)
    number is the key.
    """ 
    amicable_numbers = set()
    
    for a in range(2, number):
        d_a = d_function(a)
        d_b = d_function(d_a)
        if a == d_b and d_a > 1 and a != d_a:
            amicable_numbers.add(a)
            amicable_numbers.add(d_a)
            #print(a, d_a, d_b)
    return amicable_numbers
          
        
#print(search_divisors(220))
#print(d_function(220))
limit = 10000
amicable_numbers = search_amicable_numbers(limit)

print(amicable_numbers)
print(sum(list(amicable_numbers)))
