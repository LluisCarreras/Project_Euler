# -*- coding: utf-8 -*-
"""
Created on Fri Jan  8 00:20:28 2016

@author: Lluís


Concealed Square
Problem 206

Find the unique positive integer whose square has the form 1_2_3_4_5_6_7_8_9_0,
where each “_” is a single digit.
"""


import math

pattern = "1_2_3_4_5_6_7_8_9_0"
init = int(math.sqrt(10 * math.pow(10, 17)))
final = int(math.sqrt(19.3 * math.pow(10, 17))) + 1
result = 0

for i in range(init, final):
    i_squared_str = str(i * i)
    if i % 1000000 == 0:
        print(i_squared_str)
    indexes = range(0, 19, 2)
    got_it = True
    for index in indexes:
        if i_squared_str[index] != pattern[index]:
            got_it = False
            continue
    if got_it:
        result = i
        
print(result)