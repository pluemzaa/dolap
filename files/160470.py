nums = input("Enter a series of numbers separated by commas: ")
nums = [float(x) for x in nums.split(",")]

min_val = min(nums)
max_val = max(nums)

# ป้องกันหารศูนย์
if max_val == min_val:
    print("All numbers are the same. Normalized values: 0.00 for all.")
else:
    normalized = [(x - min_val) / (max_val - min_val) for x in nums]
    print("Normalized values:")
    for x in normalized:
        print(f"{x:.2f}")