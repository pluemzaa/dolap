m = int(input(""))
k = int(input(""))
n = int(input(""))
total = 0
total = (m*k) / n
if total % 1 == 0:
    print(total)
else:
    total =((m*k) // n)+1
    print (total)