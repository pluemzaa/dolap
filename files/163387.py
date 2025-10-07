m = int(input())
k = int(input())
n = int(input())

total = m * k
bags = total // n
if total % n > 0:
    bags += 1
print(bags)