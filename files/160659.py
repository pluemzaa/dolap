N = int(input('Enter the number of terms:'))
if N == 1:
    print(0)
elif N == 2:
    print(0,1)
elif N > 2:
    x = [0,1]
    for n in range(2,N):
        x.append(x[n - 1] + x[n - 2])
    i = 0
    while i <= n:
        print(x[i],end = ' ')
        i = i + 1