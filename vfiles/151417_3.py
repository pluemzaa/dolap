v1_str = input("Enter v1:")
v2_str = input("Enter v2:")
v1 = list(map(int, v1_str.split()))
v2 = list(map(int, v2_str.split()))

dot = sum(a*b for a,b in zip(v1,v2))
print("Dot product:", dot)