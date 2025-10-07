n = int(input("Enter number: "))
row = n
col = n  
i = j = 0
if n <= 0 :
    print("Error number must be 1 or greater")  
while i<row:
    j = 0
    while j < col:
        print(((i+j)%9)+1,sep =",",end=' ')
        j = j+1
    print()
    i = i+1