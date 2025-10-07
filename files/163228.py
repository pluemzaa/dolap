import math

m = int(input())
k = int(input()) 
n = int(input()) 

total_balls = m * k
bags_needed = math.ceil(total_balls / n)

print(bags_needed)