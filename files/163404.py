e1 = (input())
e2 = (input())
e3 = (input())

e1 = int(e1)
e2 = int(e2)
e3 = int(e3)

total = e1 * e2 + e3
bok = total - 1
bok = bok // e3
print(round(bok))