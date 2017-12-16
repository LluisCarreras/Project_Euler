# -*- coding: utf-8 -*-
"""
Created on Fri Feb  5 23:47:28 2016

@author: Lluís Carreras González

Diophantine equation
Problem 66
Consider quadratic Diophantine equations of the form:

x2 – Dy2 = 1

For example, when D=13, the minimal solution in x is 649**2 – 13×180**2 = 1.

It can be assumed that there are no solutions in positive integers when D 
is square.

By finding minimal solutions in x for D = {2, 3, 5, 6, 7}, we obtain the 
following:

3**2 – 2×2**2 = 1
2**2 – 3×1**2 = 1
9**2 – 5×4**2 = 1
5**2 – 6×2**2 = 1
8**2 – 7×3**2 = 1

Hence, by considering minimal solutions in x for D ≤ 7, the largest x is 
obtained when D=5.

Find the value of D ≤ 1000 in minimal solutions of x for which the largest 
value of x is obtained.
"""


squares = [int(i ** 2) for i in range(2, 32)]
D_list = [i for i in range(2, 1001) if i not in squares]

D_dict = {}
x = 2
max_D = 0
max_x = 0 
D_min = 2 

while len(D_dict) < 999 - len(squares):
    for y in range(1, int(x // (D_min ** 0.5) + 1)):
        D = (x ** 2 - 1)/ y ** 2        
        if D - int(D) == 0.0 and D >= 2 and D <= 1000 and D not in squares:
            if int(D) not in D_dict:
                D_dict[int(D)] = [x, y]
                if x > max_x:
                    max_x = x
                    max_D = int(D)
                D_list.remove(D)
                D_min = D_list[0]
                print("x = ", x, "\ty = ", y, "\tD = ", int(D), \
                        "\tlen = ", len(D_dict), ",\tmax_x = ", max_x,\
                        "\tD_min = ", D_min)
                print(D_list[:20])
                
#            else:
#                D_dict[int(D)] = []
#                D_dict[int(D)].append([x, y])
    x += 1
 
 
#for k in D_dict.keys():
#    print(k, "\t", D_dict[k])