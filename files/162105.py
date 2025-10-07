n = int(input("Enter number: "))

if n < 1:
    print("Error number must be 1 or greater")
else:
    for i in range(n):
        row = []
        for j in range(n):
            value = (i + 1 + j - 1) % 9 + 1
            row.append(str(value))
        print(" ".join(row))