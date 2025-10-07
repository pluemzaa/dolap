n = int(input("Enter number: "))
if n < 1:
    print("Error number must be 1 or greater")
else:
    for i in range(n):
        for j in range(n):
            num = i + j + 1
            if num > 9 :
                num = (num-1)%9+1
            print(num, end=" ")
        print()
print()