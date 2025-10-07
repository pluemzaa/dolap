i = 0
k = 0
o = int(input("Enter number: "))
for g in range(o+1):
    for i in range(o+1):
        print(k,end=' ')
        k += 1
        if k > o:
            k = 1
    print()