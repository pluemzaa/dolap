n = input("Enter number:")
if not n.isdigit() or int (n) <1:
    print("Error number must be 1 or greater")
else:
    n = int(n)
    for i in range(n):
        u = []
        for o in range(n):
            value = (i + o) % 9 + 1
            u.append(str(value))
        print(" " .join(u))