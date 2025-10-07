v1 = int(input("Enter v1 (space-separated): "))
v2 = int(input("Enter v2 (space-separated): "))

v1s = v1.split(" ")
v2s = v2.split(" ")
print(f"Dot product: {v1s[0]*v2s[0] + v1s[1]*v2s[1] + v1s[2]*v2s[2]}")