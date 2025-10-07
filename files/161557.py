n = int(input("Enter number: "))
if n < 1:
    print("Error number must be 1 or greater")
else:
    for i in range(n):
        i += 1
        for j in range(i+1):
                if j < 2:
                    print("*"*i*2,end='')
                    print()