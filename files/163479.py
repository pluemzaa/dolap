import math
s = int(input(""))
a = int(input(""))
d = int(input(""))
price = (s*a)/d
price = math.ceil(price)
print(price)