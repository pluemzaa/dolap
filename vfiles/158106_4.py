x = [0,1]
a = 2
b = 0
N = int(input("Enter the number of terms: "))
for i in range(1,N-1):
    i = x[a-1]+x[a-2]
    x.append(i)
    a += 1
for i in x:
    print(x[b],end=' ')
    b += 1