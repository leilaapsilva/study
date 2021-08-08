#!/bin/python3

# https://www.hackerrank.com/challenges/mini-max-sum

import math
import os
import random
import re
import sys

def miniMaxSum(arr):
    minimum, maximum = 0, 0
    arr.sort()
    minimum = sum(arr[:4])
    maximum = sum(arr[1:5])   
    print(minimum, maximum)
    
if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)