# -*- coding: utf-8 -*-
"""
Created on Mon Jan 18 16:51:19 2016

@author: Lluís Carreras González

Truncatable primes
Problem 37

The number 3797 has an interesting property. Being prime itself, it is 
possible to continuously remove digits from left to right, and remain prime 
at each stage: 3797, 797, 97, and 7. Similarly we can work from right to 
left: 3797, 379, 37, and 3.

Find the sum of the only eleven primes that are both truncatable from left 
to right and right to left.

NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.
"""


import math


def is_prime(num):
    """
    Evaluate wether the given number num is prime.
    """
    if num <= 1:
        return False
    else:
        for i in range(2, int(math.sqrt(num)) + 1):
            if num % i == 0:
                return False
    return True
 

def is_truncatable(num):
    """
    Evaluate wether the given number is truncatable.
    """
    
    num_str = str(num)
    for i in range(len(num_str)):
#        print(int(num_str[i:]))
#        print(int(num_str[:(len(num_str) - i)]))
        if not is_prime(int(num_str[i:])):
            return False
        if not is_prime(int(num_str[:(len(num_str) - i)])):
            return False
    return True

    
#print(is_truncatable(3797))

truncatable_nums = []
my_num = 10
while len(truncatable_nums) < 11:
    if is_truncatable(my_num):
        truncatable_nums.append(my_num)
        #print(my_num)
        len(truncatable_nums)
    my_num += 1

print(truncatable_nums)
print(sum(truncatable_nums))          