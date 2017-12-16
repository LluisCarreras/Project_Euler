# -*- coding: utf-8 -*-
"""
Created on Mon Jan 18 08:58:07 2016

@author: Lluís Carreras González

Double-base palindromes
Problem 36

The decimal number, 585 = 1001001001 (binary), is palindromic in both bases.

Find the sum of all numbers, less than one million, which are palindromic 
in base 10 and base 2.

(Please note that the palindromic number, in either base, may not include 
leading zeros.)
"""


def is_palindromic(num_str):
    """
    Returns wether the given string of digits is palindromic.
    """
    num_list = list(num_str)
    for i in range(0, int(len(num_str) / 2)):
        if num_list[i] != num_list[-(i + 1)]:
            return False
    return True
    
    
def is_palindromic_in_two_bases(num):
    """
    Returns wether the given number is palindromic in both bases 2 and 10.
    """
    
    num_base_10_str = str(num)
    num_base_2_str = str(int(str(bin(num))[2:]))
    if is_palindromic(num_base_10_str) and is_palindromic(num_base_2_str):
        print(num_base_10_str, "\t", num_base_2_str)
        return True
    return False
 
       
palindromic_nums = []
for n in range(1000000):
    if is_palindromic_in_two_bases(n):
        palindromic_nums.append(n)

print("\nNumber of palindromic numbers: ", sum(palindromic_nums))
        
#print(is_palindromic_in_two_bases(585))    