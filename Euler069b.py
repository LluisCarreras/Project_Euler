# -*- coding: utf-8 -*-
"""
Created on Sun Feb  7 11:11:55 2016

@author: Lluís Carreras González

Totient maximum
Problem 69

Euler's Totient function, φ(n) [sometimes called the phi function], is used 
to determine the number of numbers less than n which are relatively prime to
n. For example, as 1, 2, 4, 5, 7, and 8, are all less than nine and 
relatively prime to nine, φ(9)=6.

n	Relatively Prime	φ(n)	n/φ(n)
2	1	           1	2
3	1,2	           2	1.5
4	1,3	           2	2
5	1,2,3,4	     4	1.25
6	1,5	           2	3
7	1,2,3,4,5,6      6	1.1666...
8	1,3,5,7	     4	2
9	1,2,4,5,7,8	     6	1.5
10	1,3,7,9	     4	2.5
It can be seen that n=6 produces a maximum n/φ(n) for n ≤ 10.

Find the value of n ≤ 1,000,000 for which n/φ(n) is a maximum.
"""


from fractions import Fraction
import math
import time


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
    
    
def mcd_Euclides(a, b):
    """
    Return the mcd of the two given numbers a and b using Euclides' algorithm.
    """
    
    if b == 0:
        return a
    else:
        return mcd_Euclides(b, a % b)
        
        
def phi(num):
    """
    Return the phi value of the given number.
    """
    
    phi = num
    divs = divisors(num)
    if len(divs) > 0:
        for div in divs:
            phi *= 1 - Fraction(1, div)
    else:
        return num - 1
    return int(phi)
    
    
def divisors(num):
    """
    Return a list with the divisors of the given number.
    """
    divs = set()
#    divs.add(num)
    for i in range(2, num):
        if is_prime(i):
            while num % i == 0:
                divs.add(i)
                num /= i
    return divs
    
    
def allowed_divisors(num):
    """
    Return the allowed divisors given the maximum number that will be checked,
    and the product of all this divisors.
    """
    
    divs = []
    mult = 1
    test_div = 1
    while mult <= num:
        test_div += 1
        if is_prime(test_div):
            mult *= test_div
            if mult <= num:
                divs.append(test_div)
            else:
                mult /= test_div
                return divs, int(mult)
 
       
# Set the initial time
time_ini = time.time() 

top_n = 1000000

phi_dict = {}
max_phi = 0
max_n_phi = 0
max_allowed_n = allowed_divisors(top_n)[1]


for n in range(2, top_n + 1):
    if n not in phi_dict:       
        phi_n = phi(n)
        temp_dict = {}
        for k, v in phi_dict.items():
            new_n = n * k
            if new_n <= top_n:
                if mcd_Euclides(n, k) == 1:
                    new_phi = phi_n * v
                    temp_dict[new_n] = new_phi
                    n_phi = new_n / new_phi
                    if n_phi > max_phi:
                        max_phi = n_phi
                        max_n_phi = new_n
        n_phi = n / phi_n           
        phi_dict[n] = phi_n
        if n_phi > max_phi:
            max_phi = n_phi
            max_n_phi = n
        phi_dict.update(temp_dict)
#        print(n, "\t", len(phi_dict), "\t", max_phi, "\t", max_n_phi) 
        if max_n_phi >= max_allowed_n:
            break

print("Value for which n/φ(n) is a maximum: ", max_n_phi)
print("Maximum  n/φ(n): ", max_phi)
        
# Set the final time
time_end = time.time()
# Show the total required time.
time_total = time_end - time_ini
print("Required time: ", "{0:.4f}".format(time_total), "seconds") 