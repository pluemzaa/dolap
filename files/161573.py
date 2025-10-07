nums = int(input("Enter number: "))
i = j = 1
if nums < 1:
    print("Error number must be 1 or greater")
while i < nums+1:
    j = 1
    while j < nums+1:
        temp = (i+j)-1
        if temp >= 10:
            while temp >= 10:
                temp = temp-9
            print(temp, end = ' ',sep = ',')
        else:
            print(temp, end = ' ',sep = ',')
        j+=1
    print(" ")
    i+=1