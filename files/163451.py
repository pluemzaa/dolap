m = int(input(""))
k = int(input(""))
n = int(input(""))
r = m * k
r1 = r // n
if r % n != 0:
    r1 += 1
print(int(r1))