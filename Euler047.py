# -*- coding: utf-8 -*-
"""
Created on Sat Jan 23 19:14:35 2016

@author: Lluís Carreras González

Distinct primes factors
Problem 47

The first two consecutive numbers to have two distinct prime factors are:

14 = 2 × 7
15 = 3 × 5

The first three consecutive numbers to have three distinct prime factors are:

644 = 2² × 7 × 23
645 = 3 × 5 × 43
646 = 2 × 17 × 19.

Find the first four consecutive integers to have four distinct prime factors. 
What is the first of these numbers?
"""


import math


def sieve(n):
    my_primes = [i for i in range(0, n)]
    my_primes[1] = 0
    #print(int(math.sqrt(n)) + 2)
    for number in range(2, int(math.sqrt(n)) + 1, 1):
#        if number % 1000 == 0:
            #print(number)
        for prime in range(number * 2, n, number):
            if my_primes[prime] != 0:
                my_primes[prime] = 0
        #print(number, "\t", list(range(number * 2, n, number)))
        #print(number, "\t", my_primes)
    return [prime for prime in my_primes if prime != 0]
    

def divisors(num):
    """
    Return a list with the divisors of the given number.
    """
    global primes
    divs = set()
    for i in range(2, num):
        if is_prime(i):
            while num % i == 0:
                divs.add(i)
                num /= i
    return divs
    
    
def is_prime(num):
    """
    Return True if the given number num is prime.
    """
    if num <= 1:
        return False
    else:
        for i in range(2, int(math.sqrt(num)) + 1):
            if num % i == 0:
                return False
    return True
 
 
def find_distincts(num_of_consecs):
    
    continue_while = True
    idx = 9000
    
    while continue_while:
        still_correct = False
        for num in range(idx + 1, idx + num_of_consecs):
            divs_current = divisors(num)
            divs_latter = divisors(num - 1)
            
            if len(divs_current) == num_of_consecs \
                    and len(divs_latter) == num_of_consecs:
                distincts = [str(div in divs_latter) for div in divs_current]
                print(idx, "\t", num, "\t", divs_current, "\t", divs_latter)
                print(num, "\t", distincts)
                if "True" in distincts:
                    break
                elif num != idx + num_of_consecs - 1 :
                    still_correct = True
                if num == idx + num_of_consecs - 1 and still_correct:
                    result = list(range(idx, idx + num_of_consecs))
                    return result
#                    continue_while = False
        idx += 1

#primes = sieve(50000)
#print("Ya ta")
#print(primes[:15])
print(find_distincts(4))

#qty = 0
#for i in range(3, 10000):
#    if len(divisors(i)) == 4:
#        qty += 1
#    print(i, "\t", len(divisors(i)), "\t", qty)
  

