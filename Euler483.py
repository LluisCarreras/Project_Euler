# -*- coding: utf-8 -*-
"""
Created on Wed Jan 13 22:09:16 2016

@author: Lluís Carreras González

Repeated permutation
Problem 483

We define a permutation as an operation that rearranges the order of the 
elements {1, 2, 3, ..., n}. There are n! such permutations, one of which 
leaves the elements in their initial order. For n = 3 we have 3! = 6 
permutations:
- P1 = keep the initial order
- P2 = exchange the 1st and 2nd elements
- P3 = exchange the 1st and 3rd elements
- P4 = exchange the 2nd and 3rd elements
- P5 = rotate the elements to the right
- P6 = rotate the elements to the left

If we select one of these permutations, and we re-apply the same permutation 
repeatedly, we eventually restore the initial order.
For a permutation Pi, let f(Pi) be the number of steps required to restore 
the initial order by applying the permutation Pi repeatedly.
For n = 3, we obtain:
- f(P1) = 1 : (1,2,3) → (1,2,3)
- f(P2) = 2 : (1,2,3) → (2,1,3) → (1,2,3)
- f(P3) = 2 : (1,2,3) → (3,2,1) → (1,2,3)
- f(P4) = 2 : (1,2,3) → (1,3,2) → (1,2,3)
- f(P5) = 3 : (1,2,3) → (3,1,2) → (2,3,1) → (1,2,3)
- f(P6) = 3 : (1,2,3) → (2,3,1) → (3,1,2) → (1,2,3)

Let g(n) be the average value of f**2(Pi) over all permutations Pi of length n.
g(3) = (1**2 + 2**2 + 2**2 + 2**2 + 3**2 + 3**2)/3! = 31/6 ≈ 5.166666667e0
g(5) = 2081/120 ≈ 1.734166667e1
g(20) = 12422728886023769167301/2432902008176640000 ≈ 5.106136147e3

Find g(350) and write the answer in scientific notation rounded to 10 
significant digits, using a lowercase e to separate mantissa and exponent, 
as in the examples above.
"""

import math


def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return (n * factorial(n - 1))
 

def g_of_n(n):
    fact_n = factorial(n)
    g = (1 + (fact_n - 3) * math.pow(2, 2) + 2 * math.pow(n, 2)) 
    return g
    
    
def permutations(digits, my_list):
    """
    Returns the list of permutations that can be made from the objects in
    the given list.
    """
    
    if len(my_list[0]) == len(digits) and len(my_list) > 0:
        return my_list
    else:
        new_list = []
        for item in my_list:
            for digit in digits:
                if digit not in item:
                    new_item = item + digit
                    new_list.append(new_item)
        return permutations(digits, new_list)
   

     
my_list = [1, 2, 3]
my_str_list = [str(i) for i in my_list]

permu_list = permutations(my_str_list, my_str_list)
permu_list = [list(i) for i in permu_list]

print(permu_list)
    
#print(factorial(5))
#print(g_of_n(5))
    
for permu in permu_list:
    pairs = []
    for idx in range(len(permu)):
        print(permu)
        print(permu[idx])
        print(my_str_list[idx])
        if permu[idx] != my_str_list[idx]:
                        
            pair = [idx, my_str_list.index(permu[idx])]
            print(pair)
            pairs.append(pair)
            print(pairs)
            permu[pair[0]], permu[pair[1]] = permu[pair[1]], permu[pair[0]]
            print(permu)
    print(pairs)