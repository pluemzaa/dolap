n = int(input("enter number: "))

if n < 1:
    print("Error number must be 1 or greater")
else:
    for i in range(n):
        for j in range(n):
            number = (i + j) % 9+1
            print(number, end='')
        print()