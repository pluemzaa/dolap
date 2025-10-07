i = 0
k = 0
o = int(input("Enter number: "))
if o > 0:
    for g in range(o):
        for i in range(o+1):
            print(k,end=' ')
            k += 1
            if k > 9:
                k = 1
        print()
else:
    print("Error number must be 1 or greater")