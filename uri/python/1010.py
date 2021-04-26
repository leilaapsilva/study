# Not Accepted

code_1, number_1, value_1 = input().split(" ")
code_2, number_2, value_2 = input().split(" ")

code_1, code_2 = int(code_1), int(code_2)
number_1, number_2 = int(number_1), int(number_2)

value_1, value_2 = float(code_1), float(code_2)

print(number_1)
print(value_1)
print(number_2)
print(value_2)


total = number_1 * value_1 + number_2 * value_2

print("VALOR A PAGAR: R$ %0.2f" %total)