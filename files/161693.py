n = int(input("Enter number: "))
i = 1

if n < 1:
    print("Error number must be 1 or greater")
else:
    while i < n+1:
        j = 0
        while j < n:
            j = 0
            while j < n:
                if i+j > 9:
                    print((i+j-1) % 9 + 1, end=" ")
                else:
                    print(i+j, end=" ")
                j += 1
            print()
            i += 1