def calculate_dot_product():
    v1_str = input("Enter V1 (space-separated): ")
    v1 = [int(x) for x in v1_str.split()]

    v2_str = input("Enter V2 (space-separated): ")
    v2 = [int(x) for x in v2_str.split()]

    dot_product = 0
    for i in range(3):
        dot_product += v1[i] * v2[i]

    print(f"Dot product: {dot_product}")

calculate_dot_product()