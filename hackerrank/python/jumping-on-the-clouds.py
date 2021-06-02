# https://www.hackerrank.com/challenges/jumping-on-the-clouds/

# Wrong

#!/bin/python3

import math
import os
import random
import re
import sys

def jumpingOnClouds(c):
    indexes = []
    for i in range(len(c)):
        if not c[i]: # if 1
            indexes.append(i)

    print(indexes)
    
    current_cloud = indexes[0]
    
    number_jumps = 0
    for j in range(len(indexes)):
        if(indexes[j] == indexes[-1]):
            pass
        elif(indexes[j] == current_cloud + 2):
            current_cloud = indexes[j]
            number_jumps += 1
        elif(indexes[j] == current_cloud + 1):
            current_cloud = indexes[j]
            number_jumps += 1
            print(current_cloud)
        else:
            pass 
        
        print("n: ", number_jumps)
        print(current_cloud)
                    
    return number_jumps  
            
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c)

    fptr.write(str(result) + '\n')

    fptr.close()