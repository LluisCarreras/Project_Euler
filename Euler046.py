# -*- coding: utf-8 -*-
"""
Created on Sat Jan 23 18:22:38 2016

@author: Lluís Carreras González

Goldbach's other conjecture
Problem 46

It was proposed by Christian Goldbach that every odd composite number can be 
written as the sum of a prime and twice a square.

9  =  7 + 2 × 1**2
15 =  7 + 2 × 2**2
21 =  3 + 2 × 3**2
25 =  7 + 2 × 3**2
27 = 19 + 2 × 2**2
33 = 31 + 2 × 1**2

It turns out that the conjecture was false.

What is the smallest odd composite that cannot be written as the sum of a 
prime and twice a square?
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
 

def next_num(maxi):
    """
    Yields the next odd composite.
    """
    
    for n in range(2, maxi):
        if n % 2 != 0 and not is_prime(n):
            yield n
 

def is_goldbach(num):
    """
    Return true if the given number agrees with the Goldbach's other 
    conjecture.
    """
    
    primes = [i for i in range(3, num - 1) if is_prime(i)]
    for prime in primes:
        idx = 1
        while (prime + 2 * int(math.pow(idx, 2))) <= num:
            if (prime + 2 * int(math.pow(idx, 2))) == num:
                print(num, "\t", prime, "\t", idx, "\tTrue")
                return True
            idx += 1
#            print(num, "\t", prime, "\t", idx)
    print(num, "\t", prime, "\t", idx, "\tFalse")
    return False
    
    
odd_composites = next_num(100000)

idx = 1
the_next = odd_composites.__next__()
while is_goldbach(the_next): 
    print(the_next)
    the_next = odd_composites.__next__()
    
print("\nResult: ", the_next)



    