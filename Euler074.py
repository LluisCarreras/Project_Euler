# -*- coding: utf-8 -*-
"""
Created on Mon Dec 18 08:55:03 2017

@author: jlcarreras

Digit factorial chains
Problem 74 

The number 145 is well known for the property that the sum of the factorial
 of its digits is equal to 145:
1! + 4! + 5! = 1 + 24 + 120 = 145

Perhaps less well known is 169, in that it produces the longest chain of 
numbers that link back to 169; it turns out that there are only three such 
loops that exist:
169 → 363601 → 1454 → 169
871 → 45361 → 871
872 → 45362 → 872

It is not difficult to prove that EVERY starting number will eventually 
get stuck in a loop. For example,

69 → 363600 → 1454 → 169 → 363601 (→ 1454)
78 → 45360 → 871 → 45361 (→ 871)
540 → 145 (→ 145)

Starting with 69 produces a chain of five non-repeating terms, but the 
longest non-repeating chain with a starting number below one million is 
sixty terms.

How many chains, with a starting number below one million, contain exactly 
sixty non-repeating terms?

"""


import Euler_Project as ep


factorials = [ep.factorial(n) for n in range(10)]
used_sums_of_factorials = {}

def sum_digit_factorials(num):
    sum_of_factorials = 0
    for digit in str(num):
        sum_of_factorials += factorials[int(digit)]
    return sum_of_factorials

def calculate_num_chains(n):
    chains = set()
    chains.add(n)
    next_num = n
    while(True):
        #print(next_num)
        if next_num not in used_sums_of_factorials:
            chain = sum_digit_factorials(next_num)
            used_sums_of_factorials[next_num] = chain
        else:
            chain = used_sums_of_factorials[next_num]
        if chain in chains:
            return len(chains)
        else:
            chains.add(chain)
            next_num = chain

print(sum_digit_factorials(145))

max_num = 1000000

chains_60 = 0
for num in range(1, max_num + 1):
    if num % 1000 == 0:
        print(num)
    if calculate_num_chains(num) == 60:
        chains_60 += 1

print(chains_60)

#for num in range(1, max_num + 1):
    