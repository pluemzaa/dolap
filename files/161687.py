# for i in range(1,10):
#     print((i%10 ))
n = input("Enter number: ")
n = int(n)
if n < 1:
    print("Error number must be 1 or greater")
else: 
    row = col = n 
    i = 0  
    j = 0
    while i < row:
        j = 0
        while j < col:
            val = (i+1)+j
            
            if val > 9:
                val = val%9
                if val == 0:
                    val = 9
           
            print(val,sep=",",end=" ")
            j = j + 1 
           
        i = i + 1 
        print()