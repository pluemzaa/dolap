v1 = input("Enter vector 1 (space-separated, ): ")
v1 = list(map(int, v1.split()))

v2 = input("Enter vector 2 (space-separated, ): ")
v2 = list(map(int, v2.split()))

if len(v1) != 3 or len(v2) != 3:
    print("Each vector must have exactly 3 elements.")
else:
    dot_product = sum(v1[i] * v2[i] for i in range(3))
    print("Dot Product =", dot_product)