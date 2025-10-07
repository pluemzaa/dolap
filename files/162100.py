num = int(input("Enter number:"))
if num < 1:
    print("Error number must be 1 or greater")
else:
   for i in range(num):
        for n in range(num):
           value = (i+n+1)%9
           if value == 0:
               value = 9
            
           print(value, end=" ")
        print()