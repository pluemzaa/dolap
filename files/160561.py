nums = input("Enter a series of numbers separated by commas: ")
nums = [float(x.strip()) for x in nums.split(",")]

min_val = min(nums)
max_val = max(nums)

normalized = [(x - min_val) / (max_val - min_val) for x in nums]

print("Normalized values:")
for val in normalized:
    print(f"{val:.2f}")