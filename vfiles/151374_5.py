v1_input = input("Enter v1 (space-separated): ")
v1 = list(map(int, v1_input.split()))

v2_input = input("Enter v2 (space-separated): ")
v2 = list(map(int, v2_input.split()))
    dot_product = sum(v1[i] * v2[i] for i in range(3))
    print("Dot product:", dot_product)