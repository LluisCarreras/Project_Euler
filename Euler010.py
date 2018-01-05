# -*- coding: utf-8 -*-
"""
Created on Fri Jan 8 07:24:37 2016
@author: Lluís Carreras

Summation of primes
Problem 10

The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
"""


import math

def sieve(n):
    my_primes = [i for i in range(0, n)]
    my_primes[1] = 0
    print(int(math.sqrt(n)) + 2)
    for number in range(2, int(math.sqrt(n)) + 1, 1):
        if number % 1000 == 0:
            print(number)
        for prime in range(number * 2, n, number):
            if my_primes[prime] != 0:
                my_primes[prime] = 0
        #print(number, "\t", list(range(number * 2, n, number)))
        #print(number, "\t", my_primes)
    return sum(my_primes)
    
print(sieve(2000000))


