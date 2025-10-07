n = int(input("Enter number:"))
if n < 1:
    print("Error number must be 1 or greater")
else:
    for i in range(n):
        row=[]
        for j in range(n):
            num = (i+j)%9+1
            print(num if num != 0 else 9 ,end=" ")
        print()