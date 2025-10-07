# Get the first vector from the user
v1 = input("Enter vector 1 (space-separated, e.g. 1 2 3): ")
v1 = list(map(int, v1.split()))

# Get the second vector from the user
v2 = input("Enter vector 2 (space-separated, e.g. 4 5 6): ")
v2 = list(map(int, v2.split()))

# Check if both vectors have exactly 3 elements
if len(v1) != 3 or len(v2) != 3:
    print("Each vector must have exactly 3 elements.")
else:
    # Calculate dot product
    dot_product = sum(v1[i] * v2[i] for i in range(3))
    print("Dot Product =", dot_product)