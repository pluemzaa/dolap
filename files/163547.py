x = int(input(""))
y = int(input(""))
n = int(input(""))

q = (x*y)
z = q//n
if q % n > 0:
    z += 1
print(z)