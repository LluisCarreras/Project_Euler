# -*- coding: utf-8 -*-
"""
Created on Tue Feb  2 00:02:47 2016

@author: Lluís Carreras González

Powerful digit counts
Problem 63

The 5-digit number, 16807=7**5, is also a fifth power. Similarly, the 9-digit 
number, 134217728=8**9, is a ninth power.

How many n-digit positive integers exist which are also an nth power?
"""

import time


time_ini = time.time()
   
expo = 1
count = 0

# The limit 25 is found experimentally.
while expo < 25:
    base_num = 1
    while True:
        my_num = base_num ** expo
        len_num = len(str(my_num))
        if len_num == expo:
            count += 1
            print(count, "\t", my_num, "\t", base_num, "\t", expo)
        elif len_num > expo:
            break
        base_num  += 1
    expo += 1

time_end = time.time()
time_total = time_end - time_ini
print("Time required: \t", "{0:.4f}".format(time_total), "seconds")   