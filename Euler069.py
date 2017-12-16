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
import Euler_Project as ep
import time


def mcd_Euclides(a, b):
    """
    Return the mcd of the two given numbers a and b using Euclides' algorithm.
    """
    
    if b == 0:
        return a
    else:
        return mcd_Euclides(b, a % b)
        
        
def is_coprime(a, b):
    """
    Return True if a is coprime with b.
    """
    
    return mcd_Euclides(a, b) == 1
    

def are_coprime(a, b, primes):
    for prime in primes:
        if prime < a and prime < b:
            if a % prime == 0 and b % prime == 0:
                return False
        else:
            return True
    return True
    
def are_cop(a, b):
    return len(set(ep.divisors(a)).intersection(set(ep.divisors(b)))) == 1
    
    
def phi(num):
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
        if ep.is_prime(i):
            while num % i == 0:
                divs.add(i)
                num /= i
    return divs

primes = ep.sieve(1000001)
last_prime = primes[-1]

max_n = last_prime 
max_phi = phi(last_prime)
       
for n in range(last_prime, 1000001):
    new_phi =phi(n)
    if new_phi > max_phi:
        max_phi = new_phi
        max_n = n
    print(n, "\t", phi(n), "\t", max_phi, "\t", max_n)
    
print(max_phi, "\t", max_n)



## Set the initial time
#time_ini = time.time() 
#
#top_n = 1000000
#
#print("Before sieve")
##primes = ep.sieve(1000001)
#divisors = {}
#for k in range(1, top_n + 1):
##    divisors[k] = [1]
##    divisors[k].append(k)
#    divisors[k] = list(ep.divisors(k))
#    divisors[k].append(1)
#    divisors[k].append(k)
#    print(k)
##divisors[2].add(2)
#print("After sieve")
#print(divisors)
#
#phi_dict = {}
#for n in range(2, top_n + 1):
#    if n % 1000 == 0:
#        print(n)
#    for i in range(1, n):
##        if is_coprime(i, n):
#        if len(set(divisors[i]).intersection(set(divisors[n]))) == 1:
#            if n in phi_dict:
#                phi_dict[n].append(i)
#            else:
#                phi_dict[n] = [i]
#print(phi_dict)
#                
#for key in phi_dict.keys():
#    phi = len(phi_dict[key])
#    phi_dict[key] = [phi] 
#    phi_dict[key].append(key / phi)
#
#max_n_phi = 0
#max_n = 0
#for k, v in phi_dict.items():
#    print(k, "\t", v[0], "\t", v[1])
#    if v[1] > max_n_phi:
#        max_n_phi = v[1]
#        max_n = k
#
#print("Maximum n/φ(n):                              ", max_n_phi)
#print("n ≤ 1,000,000 for which n/φ(n) is a maximum: ", max_n)
#
## Set the final time
#time_end = time.time()
## Show the total required time.
#time_total = time_end - time_ini
#print("Required time: ", "{0:.4f}".format(time_total), "seconds")       