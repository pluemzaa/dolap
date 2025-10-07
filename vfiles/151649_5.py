v1 = list(map(int, input("Enter v1: ").split()))
v2 = list(map(int, input("Enter v2: ").split()))
s = sum([a*b for a, b in zip(v1, v2)])
print(s)