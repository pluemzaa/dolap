n = int(input("Enter number: "))

if n >= 1:
    i = 1
    while i <= n:
        j = 1
        num = i
        while j <= n:
            print(num, end=' ')
            num+= 1
            if num > 9:
                num = 1
            j+= 1
        print()
        i += 1
else:
    print("Error number must be 1 or greater")