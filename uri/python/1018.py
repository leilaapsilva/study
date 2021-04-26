# Accepted

v = int(input())

n100 = v // 100
value = v % 100
n50 = value // 50
value = value % 50
n20 = value // 20
value = value % 20
n10 = value // 10
value = value % 10
n5 = value // 5
value = value % 5
n2 = value // 2
value = value % 2
n1 = value // 1

print("%d" %v)
print("%d nota(s) de R$ 100,00" %n100)
print("%d nota(s) de R$ 50,00" %n50)
print("%d nota(s) de R$ 20,00" %n20)
print("%d nota(s) de R$ 10,00" %n10)
print("%d nota(s) de R$ 5,00" %n5)
print("%d nota(s) de R$ 2,00" %n2)
print("%d nota(s) de R$ 1,00" %n1)