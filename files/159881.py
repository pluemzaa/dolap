N = int(input('Enter a number (enter 0 to stop):'))
i = 1
x = 0
if N != 0:
    while N != 0:
        x = (x + N) / i
        i = i + 1
        N = int(input('Enter a number (enter 0 to stop):'))
    print(x)
else:
    print('No numbers entered')