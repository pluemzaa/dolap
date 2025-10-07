n = int(input("Enter number:"))
if n >= 1:
    c = 0
    i = 0
    while i < n:
        j = 0
        c = 1
        v = 1
        while j < n:
            if i+j+1 < 10:
                print(i+j+1, end=" ", sep=',')
            elif c < 10:
                print(c, end=" ", sep=',')
                c += 1
            elif v<10:
                print(v, end=" ", sep=',')

            j += 1
        print("")
        i += 1
else:
    print("Error number must be 1 or greater")