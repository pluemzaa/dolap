n=int(input("Enter number:"))
if n<1:
    print("Error number must be 1 or greater")
else:
    for i in range(1,n+1):
        a="*"*(2*i)
        print(a)
        print(a)