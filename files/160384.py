print("Enter a series of numbers separated by commas:", end=" ")
input_str = input()
nums = [float(x.strip()) for x in input_str.split(",")]

min_val = min(nums)
max_val = max(nums)

print("Normalized values:")
for x in nums:
    norm = (x - min_val) / (max_val - min_val)
    print(f"{norm:.2f}")