vec1 = input("Enter v1 (space-separated): ")
vec2 = input("Enter v2 (space-separated): ")

v1 = list(map(int, vec1.split()))
v2 = list(map(int, vec2.split()))

if len(v1) != len(v2):
    print("Dot product")
else:
    dot = sum(a * b for a, b in zip(v1, v2))
    print("Dot product =", dot)