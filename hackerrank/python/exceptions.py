# https://www.hackerrank.com/challenges/exceptions

t = int(input())

for i in range(t):
    a, b = input().split(" ")
    try:
        a, b = int(a), int(b)
        print(a//b)
    except BaseException as e:
        print("Error Code:", e)