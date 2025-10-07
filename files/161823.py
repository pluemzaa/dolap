num = int(input("Enter number: "))
if num < 1:
    print("Error number must be 1 or greater")
else:      
    for row in range(num):
            row += 1
            for col in range(num+1):
                if col < 2:
                    print("*"*row*2, end=" ")
                    print()