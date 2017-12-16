# -*- coding: utf-8 -*-
"""
Created on Sat Jan 16 18:44:07 2016

@author: Lluís Carreras González

Coin sums
Problem 31

In England the currency is made up of pound, £, and pence, p, and there are 
eight coins in general circulation:

1p, 2p, 5p, 10p, 20p, 50p, £1 (100p) and £2 (200p).
It is possible to make £2 in the following way:

1×£1 + 1×50p + 2×20p + 1×5p + 1×2p + 3×1p

How many different ways can £2 be made using any number of coins?
"""


total = 200
ways = 0


for p1 in range(0, total + 1):
    p = [p1]
    v = [1]
    value = sum([p[i] * v[i] for i in range(len(p))])
    if value == total:
        ways += 1
        print(p, "\t", ways)
        continue
    elif value > total:
        break
    
    for p2 in range(0, total + 1):
        p = [p1, p2]
        v = [1, 2]
        value = sum([p[i] * v[i] for i in range(len(p))])
        if value == total:
            ways += 1
            print(p, "\t", ways)
            continue
        elif value > total:
            break
        
        for p5 in range(0, total + 1):
            p = [p1, p2, p5]
            v = [1, 2, 5]
            value = sum([p[i] * v[i] for i in range(len(p))])
            if value == total:
                ways += 1
                print(p, "\t", ways)
                continue
            elif value > total:
                break         
                
            for p10 in range(0, total + 1):
                p = [p1, p2, p5, p10]
                v = [1, 2, 5, 10]
                value = sum([p[i] * v[i] for i in range(len(p))])
                if value == total:
                    ways += 1
                    print(p, "\t", ways)
                    continue
                elif value > total:
                    break
               
                for p20 in range(0, total + 1):
                    p = [p1, p2, p5, p10, p20]
                    v = [1, 2, 5, 10, 20]
                    value = sum([p[i] * v[i] for i in range(len(p))])
                    if value == total:
                        ways += 1
                        print(p, "\t", ways)
                        continue
                    elif value > total:
                        break
                    
                    for p50 in range(0, total + 1):
                        p = [p1, p2, p5, p10, p20, p50]
                        v = [1, 2, 5, 10, 20, 50]
                        value = sum([p[i] * v[i] for i in range(len(p))])
                        if value == total:
                            ways += 1
                            print(p, "\t", ways)
                            continue
                        elif value > total:
                            break
                        
                        for p100 in range(0, total + 1):
                            p = [p1, p2, p5, p10, p20, p50, p100]
                            v = [1, 2, 5, 10, 20, 50, 100]
                            value = sum([p[i] * v[i] for i in range(len(p))])
                            if value == total:
                                ways += 1
                                print(p, "\t", ways)
                                continue
                            elif value > total:
                                break
                           
                            for p200 in range(0, total + 1):
                                p = [p1, p2, p5, p10, p20, p50, p100, p200]
                                v = [1, 2, 5, 10, 20, 50, 100, 200]
                                value = sum([p[i] * v[i] for i in range(len(p))])
                                if value == total:
                                    ways += 1
                                    print(p, "\t", ways)
                                    continue
                                elif value > total:
                                    break


print(ways)                       