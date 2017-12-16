# -*- coding: utf-8 -*-
"""
Created on Thu Jan  7 17:34:34 2016

@author: Lluís


Largest palindrome product
Problem 4

A palindromic number reads the same both ways. The largest palindrome made 
from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""

import math

def largest_palindrome(num_digits):
    largest = 1
    for i in range(int(math.pow(10, num_digits -1)), int(math.pow(10, num_digits)), 1):
        for j in range(int(math.pow(10, num_digits - 1)), int(math.pow(10, num_digits)), 1):
            item = i * j
            if item > largest:
                larg_str = str(item)
                pali_str = ""
                for q in range(len(larg_str) - 1, -1, -1):
                    pali_str = pali_str + larg_str[q]
                #print(i, "    ", j, "    ", larg_str, "    ", pali_str, "  ", item)
                if int(larg_str) == int(pali_str):
                    largest = item
                    #print(larg_str)
    return largest
    
print(largest_palindrome(2))
print(largest_palindrome(3))