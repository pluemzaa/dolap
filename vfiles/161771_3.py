n = int(input("Enter number: "))

if n < 1:
    print("Error number must be 1 or greater")
else:
    for row in range(1, n + 1):
        line = []
        for col in range(n):
            num = (row + col - 1) % 9 + 1
            line.append(str(num))
        print(' '.join(line))