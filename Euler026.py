# -*- coding: utf-8 -*-
"""
Created on Wed Jan 13 18:27:30 2016
@author: Lluís Carreras González

Reciprocal cycles
Problem 26

A unit fraction contains 1 in the numerator. The decimal representation of 
the unit fractions with denominators 2 to 10 are given:

1/2	= 	0.5
1/3	= 	0.(3)
1/4	= 	0.25
1/5	= 	0.2
1/6	= 	0.1(6)
1/7	= 	0.(142857)
1/8	= 	0.125
1/9	= 	0.(1)
1/10	= 	0.1

Where 0.1(6) means 0.166666..., and has a 1-digit recurring cycle. It can be 
seen that 1/7 has a 6-digit recurring cycle.

Find the value of d < 1000 for which 1/d contains the longest recurring 
cycle in its decimal fraction part.
"""


from decimal import Decimal, getcontext

# Set the precission to 10000
getcontext().prec = 10000

lng_max_rec_cycle = 1
d = 2
    
for num in range(2, 1000):
    fraction = str(Decimal(1) / Decimal(num))[2:]
    
    for lng in range(2, 4000):
        if fraction[50:(50+lng)] == fraction[(50+lng):(50+2*lng)]:
            if lng > lng_max_rec_cycle:
                lng_max_rec_cycle = lng
                d = num
            break

print(d, lng_max_rec_cycle)    
   
    
    
