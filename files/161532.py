nums = int(input("Enter number: "))
if nums > 0:
    for i in range(1,nums+1):
        for j in range(2): 
            print("*" * (i*2))
else:
    print("Error number must be 1 or greater")