x = int(input("Enter number: "))
s=0
i = 0
y=0
if x <= 0 :
    print("Error number must be 1 or greater")
else :
    while i <x:
        if y >=9:
            y=0
        s=0
        k=1
        for j in range(x):
            if (j+y)+1 >= 10:
                if k >= 10:
                    k=1
                    print(f"{k} ",end='')
                    k+=1
                else:
                    print(f"{k} ",end='')
                    k+=1
            else:
                print(f"{(j+y)+1} ",end='')
                s+=1
        print()
        y+=1
        i+=1