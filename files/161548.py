n = int(input("Enter number: "))

if n < 1:
    print("Error number must be 1 or greater")
else:
    for step in range(1, n + 1):
        s = '*' * (step * 2)
        print(s)
        print(s)