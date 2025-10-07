nums = input("Enter a series of numbers separated by commas:")
nums = [float(x) for x in nums.split(",")]

min_val = min(nums)
max_val = max(nums)

if max_val == min_val:
    print("All numbers are the same. Normalized values: 0.00 for all.")
else:
    normalize = [(x - min_val) / (max_val - min_val) for x in nums]
    print("Normalized calues:")
    for x in normalize:
        print(f"{x:.2f}")