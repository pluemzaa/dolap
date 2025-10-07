n = int(input("Ente number : "))

if n < 1 :
    print(" Error number must be 1 or greater")
else :
    i = 1
    while i <= n :
        num =1 
        j =1
        while j < n :
            print(num, end='')
            num += 1
            if num > 9 :
                num =1
            j+= 1
        print()
        i += 1