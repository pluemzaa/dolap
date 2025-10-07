n = int(input("Enter number: "))

if n < 1:
    print("Error number must be 1 or greater")
else:
    for i in range(1, n+1):
        for j in range(i, i+n):
            num = j % 9
            if num == 0:
                num = 9
            print(num, end=" ")
        print()