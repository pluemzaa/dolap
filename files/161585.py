z = int(input("Enter number:"))
i = j = 0
if z < 1:
    print("Error number must be 1 or greater")
else:
    for i in range(z):
        row=[]
        for j in range(z):
            x = (i+j+1)
            if x > 9:
                x = (x-1)%9+1
            row.append(str(x))
        print("".join(row))