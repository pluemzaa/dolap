# Prompt the user to enter the first vector
v1 = list(map(int, input(”Enter v1 (3 space-separated integers): “).split()))

# Prompt the user to enter the second vector
v2 = list(map(int, input(”Enter v2 (3 space-separated integers): “).split()))

# Calculate the dot product: sum of v1[i] * v2[i]
dot_product = sum(a * b for a, b in zip(v1, v2))

# Print the result
print(”Dot product:“, dot_product)