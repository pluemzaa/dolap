x = int(input("Enter number: "))
if x < 1:
    print("Error number must be 1 or greater")
else:
    for i in range(x):
        for j in range(1, x + 1):
            c = i + j
            if c <= 9:
                print(c, end=" ")
            else:
                c = c % 9
                if c == 0:
                    c = 9
                print(c, end=" ")
        print()