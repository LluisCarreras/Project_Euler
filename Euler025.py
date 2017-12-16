# -*- coding: utf-8 -*-
"""
Created on Wed Jan 13 18:11:20 2016

@author: Lluís Carreras González

1000-digit Fibonacci number
Problem 25

The Fibonacci sequence is defined by the recurrence relation:

Fn = Fn−1 + Fn−2, where F1 = 1 and F2 = 1.
Hence the first 12 terms will be:

F1 = 1
F2 = 1
F3 = 2
F4 = 3
F5 = 5
F6 = 8
F7 = 13
F8 = 21
F9 = 34
F10 = 55
F11 = 89
F12 = 144
The 12th term, F12, is the first term to contain three digits.

What is the index of the first term in the Fibonacci sequence to contain 
1000 digits?
"""


def fibonacci_digits(n):
    """
    Returns the index of the first term in the Fibonacci sequence to contain 
    n digits
    """
    
    f1 = 1
    f2 = 1
    index = 2
    while len(str(f1 + f2)) < n:
        index += 1
        f_next = f1 + f2
        f1, f2 = f2, f_next
    return index + 1


print(fibonacci_digits(1000))    
        
