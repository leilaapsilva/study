# https://www.hackerrank.com/challenges/time-conversion

# Wrong

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def timeConversion(s):
    # Write your code here
    ampm = s[-2:]
    t = s[:-2].split(":")
    print(t)
    
    if (ampm == 'PM'):
        new = int(t[0]) + 12
        return str(new)+ ":" + t[1]+ ":" + t[2]
    else:
        return t[0]+":"+t[1]+":"+t[2]
        
    #print(ampm)
    #print(t)
    #return ampm 

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()
