x = input("Enter v1 (space-separated): ").split()
c = input("Enter v2 (space-separated): ").split()
result = int(x[0]) * int(c[0]) + int(x[1]) * int(c[1]) + int(x[2]) * int(c[2])
print("Dot product:", result)