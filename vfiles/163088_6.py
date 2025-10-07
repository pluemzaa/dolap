import math

m = int(input(''))
l = int(input(''))
t = int(input(''))

sol = (m * l) / t
sol = math.ceil(sol)

print(sol)