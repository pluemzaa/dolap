a = int(input())
b = int(input())
c = int(input())
d = a*b
e = d // c
if d % c != 0:
    e = e + 1
print(e)