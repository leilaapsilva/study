# https://www.hackerrank.com/challenges/map-and-lambda-expression

#def fibonacci(n):
#    if(n==0):
#        return 0
#    elif(n==1 or n==2):
#        return 1
#    else:
#        return fibonacci(n-2) + fibonacci(n-1)

cube = lambda x: x*x*x

def fibonacci(n):
   if(n==0):
       return []
   elif(n==1): 
       return [0]
   elif(n==2):
       return [0,1]
   else:
       l = [0,1]
       for i in range(2, n):
           l.append(l[i-1]+l[i-2])
       return l
        
if __name__ == '__main__':
    n = int(raw_input())
    print map(cube, fibonacci(n))