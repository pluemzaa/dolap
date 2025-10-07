n = int(input("Ente number : "))
if n >= 1 :
    for i in range(1,n+1) :
        for j in range(2) :
            print(i*"**")
else : 
    print("Error number must be 1 or greater")