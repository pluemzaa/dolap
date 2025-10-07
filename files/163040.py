import math

m = int(input())
k = int(input())
n = int(input())

total_ = m * k

bags = math.ceil(total_ / n)

print(bags)