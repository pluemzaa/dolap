import math
m = int(input())  
k = int(input()) 
n = int(input())  

total_needed = m * k
needed_bags = math.ceil(total_needed / n)
print(needed_bags)