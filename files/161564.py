n = int(input("Enter number: "))
if n < 1:
    print("Error number must be 1 or greater")
else:
    for i in range(n):
        for j in range(n):
            a = (i + j + 1) %9
            if a == 0:
                a = 9
            print(a, end=' ')
        print()