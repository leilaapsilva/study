# https://www.hackerrank.com/challenges/np-array-mathematics

import numpy

n, m = map(int, input().split())

a = []
for i in range(n):
    itens = list(map(int, input().split()))
    a.append(itens)

b = []
for i in range(n):
    itens = list(map(int, input().split()))
    b.append(itens)

a = numpy.array(a, int)    
b = numpy.array(b, int)     

print(a+b) 
print(a-b)   
print(a*b)
print(a//b)
print(a%b)
print(a**b)