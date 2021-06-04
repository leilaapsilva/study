# https://www.hackerrank.com/challenges/best-divisor/

# Wrong

#!/bin/python3

import math
import os
import random
import re
import sys

if __name__ == '__main__':
    n = int(input().strip())

    # find number divisors:
    i = 1
    divisors = []
    while i <= n:
        if(n%i==0):
            divisors.append(i)
        i = i + 1
        
    for d in divisors:
        s = str(d)
            
    print(divisors)