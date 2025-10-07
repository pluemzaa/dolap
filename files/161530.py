#1
x = int(input("Enter number: "))
if x <= 0 :
    print ("Error number must be 1 or greater")
else :
    for i in range (x) :
        for j in range((i+1)*2) :
            print("*",end = "")
        print()
        for k in range((i+1)*2) :
            print("*",end = "")
        print()