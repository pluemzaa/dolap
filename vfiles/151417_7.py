v1 = input("Enter vector 1 (space-separated, e.g. 1 2 3): ")
v1 = list(map(int, v1.split()))

v2 = input("Enter vector 2 (space-separated, e.g. 4 5 6): ")
v2 = list(map(int, v2.split()))

if len(v1) != 3 or len(v2) != 3:
    print("Each vector must have exactly 3 elements.")
else:
    dot_product = sum(v1[i] * v2[i] for i in range(3))
    print("Dot Product =", dot_product)