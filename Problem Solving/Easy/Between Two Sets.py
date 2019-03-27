#!/bin/python3

from functools import reduce
from fractions import gcd

def LCM(a,b):
    return (a*b)//gcd(a,b)

def getTotalX(a,b):
    
    lcm = reduce(LCM, a, 1)
    _gcd = reduce(gcd, b) 

    lcm_copy = lcm

    count = 0
    while lcm <= _gcd:
        if(_gcd % lcm) == 0:
            count += 1
        lcm = lcm + lcm_copy

    return count
