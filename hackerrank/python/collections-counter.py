# https://www.hackerrank.com/challenges/collections-counter/

# Wrong

number_of_shoes = int(input())
shoe_sizes = list(input().split(" "))
number_of_customers = int(input())

sizes, prices = [], []
for i in range(number_of_customers):
    size, price = input().split(" ")
    sizes.append(size)
    prices.append(price)

print(sizes)
print(prices)    
    
money = 0
j = 0
for s in sizes:
    if s in shoe_sizes:
        money += int(prices[j])    
        prices.remove(prices[j])
        shoe_sizes.remove(s)
        sizes.remove(s)
    j=j+1  

    
print(number_of_shoes)
print(shoe_sizes)
print(number_of_customers)
print(sizes)
print(prices)
print(money)