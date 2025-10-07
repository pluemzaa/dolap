nums = input("Enter a series of numbers separated by commas: ")
x = [float(i) for i in nums.split(",")]

min_x = min(x)
max_x = max(x)


if max_x != min_x:
    x_scaled = [(i - min_x) / (max_x - min_x) for i in x]
else:
    x_scaled = [0 for i in x]

print("Normalized values:")
for v in x_scaled:
    print(f"{v:.2f}")