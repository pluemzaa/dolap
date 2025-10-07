v1 = input("Enter v1 (space-separated): ").split()
v2 = input("Enter v2 (space-separated): ").split()

v1 = [int(pls) for pls in v1]
v2 = [int(pls) for pls in v2]

dot = sum(v1[tt] * v2[tt] for tt in range(3))

print("Dot product: ", dot )