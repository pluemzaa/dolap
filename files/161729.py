n = int(input("Enter number: "))
i = j = 1
if n < 1 :
    print ("Error number must be 1 or greater")
while i < n+1 :
    j = 1
    while j < n+1:
        t = (i+j)-1
        if t >= 10:
            while t >= 10 :
                t -= 9
            print(t,end = ' ',sep=',')
        else:
            print(t,end = ' ',sep = ',')
        j+=1
    print(" ")
    i+=1