# https://www.hackerrank.com/challenges/polar-coordinates

# Wrong 

c = input()
x, y = c.split("+") # real and imaginary parts

x = int(x)
y = int(y[:-1])

print(x)
print(y)

test = complex(x, y)
print(test)