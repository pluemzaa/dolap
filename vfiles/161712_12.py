n = int(input("Enter number: "))
if n < 1:
    print("error number must be 1 or greater")
else:
    for i in range(n):
        for j in range(n):
            num = i * 9 + j + 1
            print(num % 9 + 1, end=" ")
        print()
print()