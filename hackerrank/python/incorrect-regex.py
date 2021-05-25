# www.hackerrank.com/challenges/incorrect-regex

import re

t = int(input())
for i in range(t):
    s = input()
    try:
        re.compile(s)
        is_valid = True
    except re.error:
        is_valid = False    
    print(is_valid)