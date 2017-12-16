# -*- coding: utf-8 -*-
"""
Created on Sat Jan 30 15:45:46 2016

@author: Lluís Carreras González

Square root convergents
Problem 57

It is possible to show that the square root of two can be expressed as an 
infinite continued fraction.

√ 2 = 1 + 1/(2 + 1/(2 + 1/(2 + ... ))) = 1.414213...

By expanding this for the first four iterations, we get:

1 + 1/2 = 3/2 = 1.5
1 + 1/(2 + 1/2) = 7/5 = 1.4
1 + 1/(2 + 1/(2 + 1/2)) = 17/12 = 1.41666...
1 + 1/(2 + 1/(2 + 1/(2 + 1/2))) = 41/29 = 1.41379...

The next three expansions are 99/70, 239/169, and 577/408, but the eighth 
expansion, 1393/985, is the first example where the number of digits in the 
numerator exceeds the number of digits in the denominator.

In the first one-thousand expansions, how many fractions contain a numerator 
with more digits than denominator?
"""


from fractions import Fraction

count = 0
my_num = 1 + Fraction(1, 2)

for n in range(1000):
    numerator = my_num. numerator
    denominator = my_num.denominator
    if len(str(numerator)) > len(str(denominator)):
        count += 1
    my_num = 1 + Fraction(1, 1 + my_num)
    
print(count)    


