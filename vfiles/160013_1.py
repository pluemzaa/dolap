N = int(input('Enter a number N:'))
for num in range(1, N + 1):
    i = 2
    while i < num and num % i != 0:
        i = i +1
    if i == num:
        print(num)