_v1 = input("Enter v1 (space-separated): ")
_v2 = input("Enter v2 (space-separated): ")

v1 = _v1.split(" ")
v2 = _v2.split(" ")

dotproduct = (v1[0] * v2[0]) + (v1[1] * v2[1]) + (v1[2] * v2[2])

print(f"Dot product: {dotproduct}")