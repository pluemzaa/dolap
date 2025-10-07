N = int(input("Enter the number of terms:"))
temp = 0;
i = 0;
mySum = 0;
j = 1;

#if N > 1 :
#   print("0",end=" ")
#else :
#    print("An error has occurred idk what happened")
#    exit()

while j <= N :
    mySum = i + temp 
    print(mySum,end=' ')
    temp = i
    i = mySum
    if i == 0 :
        i = 1
        print(1,end=' ')
        N -=1
    j+=1