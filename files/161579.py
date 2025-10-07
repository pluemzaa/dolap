n = int(input("Enter number: "))
if n < 1:
    print("Error number must be 1 or greater")
else:
    for i in range(1,n + 1):
        num = i
        for j in range(n):
            
            if num > 9:
                num = num - 9
            print(num ,end=' ')
            num = num + 1
        print()