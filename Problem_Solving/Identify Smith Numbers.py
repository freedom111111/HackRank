#!/bin/python3

import os
import sys

# Complete the solve function below.

def summ(n):
    return sum([int(x) for x in list(str(n))])
    
def solve(n):
    sum1 = summ(n)
    print(sum1)
    factor = 2
    sum2 = 0
    while n !=1:
        if n%factor==0:
            sum2 += summ(factor)
            n = n/factor
        else:
            factor += 1 
    return int(sum1==sum2)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    result = solve(n)

    fptr.write(str(result) + '\n')

    fptr.close()
