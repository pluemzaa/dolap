import math

m = int(input())
k = int(input())
n = int(input())

total_meatballs = m * k
bags_needed = math.ceil(total_meatballs /n)

print(bags_needed)