n = int(input("Enter number:"))

if n <= 0:
    print("Error number must be 1 or greater")
    
for i in range(n):
    for i in range(i+1):
        print("**")
        print("**")
    print("")