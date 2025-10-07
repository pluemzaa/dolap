n = int(input("Enter number:"))

if n <= 0:
    print("Error number must be 1 or greater")
else:
        
    for i in range(1,n+1):
        s = ("*" * 2)*i
        print(s)
        print(s)