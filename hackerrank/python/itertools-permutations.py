# https://www.hackerrank.com/challenges/itertools-permutations

# Wrong - 1/6 test cases failed :c

from itertools import permutations

s, k = input().split(" ")
k = int(k)

p = permutations(list(sorted(s)),k)

for item in p:
    print("".join(str(item)[2:-2].split("', '")))