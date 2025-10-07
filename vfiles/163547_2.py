x = int(input(""))
y = int(input(""))
n = int(input(""))

q = (x*y)//n
if q != (x / y):
    q += 1
    print(q)