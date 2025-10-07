m = int(input(""))
k = int(input(""))
n = int(input(""))

total = m*k
b = total // n
if total % n > 0:
    b += 1
print(b)