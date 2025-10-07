num=int(input("Enter number:"))
if num < 1:
    print("Error number must be 1 or greater")
else:
    for i in range(1,num+1):
        s=2*i
        for i in range(2):
            print("*"*s)
    print()