n = int(input())

if n < 1:
    print("Error number must be 1 or greater")
else:
    for row in range(1, n+1):
        num = row
        for col in range(n):
            if num > 9:
                num = 1
            print(num, end=' ')
            num += 1
        print()