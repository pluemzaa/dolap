y = int(input("Enter number: "))
i = j = 1
if y < 1 :
    print ("Error number must be 1 or greater")
while i < y+1 :
    j = 1
    while j < y+1:
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