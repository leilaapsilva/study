# https://www.hackerrank.com/challenges/np-zeros-and-ones

import numpy

shape = tuple(map(int, input().split()))

print(numpy.zeros((shape), dtype=numpy.int))
print(numpy.ones((shape), dtype=numpy.int))