m = int(input())
k = int(input())
n = int(input())
if (m*k) % n == 0:
    print((m*k) // n)
else:
    print(((m*k) // n )+ 1)