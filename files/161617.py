num = int(input("Enter number : "))

i = 1
if num >= 1 :
    while i <= num :
        j = 0
        while j < num:
            print(((i+j-1)%9)+1,end ='')
            j+=1
        print()
        i += 1
else :
    print("Error number must be 1 or greater")