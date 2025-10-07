n = int(input("Enter number: "))

if n < 1:
    print("Error number must be 1 or greater")
else:
    for i in range(n):
        start = i + 1
        for j in range(n):
            num = (start + j - 1) % 9 + 1  # วนเลข 1-9
            print(num, end=" ")
        print()