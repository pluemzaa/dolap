a = int(input())
b = int(input())
c = int(input())

total = a * b
bags = (total + c - 1) // c
print(bags)