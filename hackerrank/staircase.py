#!/bin/python3

# https://www.hackerrank.com/challenges/staircase

import math
import os
import random
import re
import sys

def staircase(n):
    for i in range(n):
        print((n-i-1)*' ' + (i+1)*'#')

if __name__ == '__main__':
    n = int(input().strip())

    staircase(n)