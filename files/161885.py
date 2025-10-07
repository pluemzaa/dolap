num = input("Enter number: ")
num = int(num)
if num < 1:
    print("Error number must be 1 or greater")
else:
    for i in range(num):
    
        for k in range(2):
            amt = (i+1)*2
            print("*"*amt)