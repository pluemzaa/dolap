N = int(input('Enter the number of rows for the pyramid: '))
x = 0
if 1 <= N <= 50:
    for i in range(1, N+1):
        x += i
    print(f'The total number of boxes: {x}')

    if x % 2 == 0:
        print('The total number of boxes is even')
        for j in range(1, N+1):
            print(' '.join([str(j)] * j))
    else:
        print('The total number of boxes is odd')
        for k in range(N, 0, -1):
            print(' '.join([str(k)] * k))