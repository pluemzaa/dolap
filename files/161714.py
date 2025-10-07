nums = int(input("Enter number: "))
row = nums
col = nums
i = j = 0
if nums < 1:
    print("Error number must be 1 or greater")
else:
    while i < row:
        j=0
        while j < col:
            if i+j>=9:
                print((i+j) % 9+1,end=' ') 
            else:
                print(i+j+1,end=' ')
            j=j+1
        i=i+1
        print(' ')