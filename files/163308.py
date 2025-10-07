row = int(input("Enter the number of rows for the pyramid: "))

boxnum = 0
for i in range(0,row+1):
    for j in range(i):
        boxnum += 1
    
print(f"The total number of boxes: {boxnum}")
t = "odd" if boxnum % 2 != 0 else "even"
print(f"The total number of boxes is {t}")

if t == "odd":
    for i in range(row,0,-1):
        for j in range(i):
            print(f"{i} ",end="")
            # boxnum += 1
        print()
else :
    for i in range(1,row+1):
        for j in range(i):
            print(f"{i} ",end="")
            #  boxnum += 1
        print()