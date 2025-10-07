n = int(input("Enter number:"))
if n < 1:
    print("Error number must be 1 or greater")
else:
    for i in range(1,n+1):
        for j in range(n):
            num = (1+j)%9
            print(num if num != 0 else 9 ,end=" ")
        print()