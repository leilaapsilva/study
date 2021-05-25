# https://www.hackerrank.com/challenges/np-eye-and-identity

import numpy
numpy.set_printoptions(legacy='1.13')

n, m = input().split()
n, m = int(n), int(m)

print(numpy.eye(n,m, k=0))