m = int(input())
n = int(input())
k = int(input())

num = (m*n)

if num % k == 0:
    print(int((m*n)/k))
else:
    print(int((m*n)/k) + 1)