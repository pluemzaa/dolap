x=int(input(""))
y=int(input(""))
z=int(input(""))
a = x*y
s = a // z
if a % z != 0:
    s = s + 1
print(s)