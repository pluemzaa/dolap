mb = int(input(""))
n = int(input(""))
p = int(input(""))
r1 = mb*n
r2 = r1/p
if r1 % p != 0:
    r2 += 1
print(int(r2))