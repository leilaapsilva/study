#!/bin/python3

# https://www.hackerrank.com/challenges/plus-minus

import math
import os
import random
import re
import sys

def plusMinus(arr):
    positives, negatives, zeros = 0, 0, 0
    tam = len(arr)
    
    for i in arr:
        if i > 0:
            positives += 1
        elif i < 0:
            negatives += 1
        else:
            zeros += 1
    
    r_positives = positives / tam 
    r_negatives = negatives / tam
    r_zeros = zeros / tam 
    
    print("{:1.6f}".format(r_positives))
    print("{:1.6f}".format(r_negatives))
    print("{:1.6f}".format(r_zeros))

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
