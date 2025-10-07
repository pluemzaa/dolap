nums = input("Enter a series of numbers separated by commas: ")
nums = [int(n) for n in nums.split(',')]

min_val = min(nums)
max_val = max(nums)

print("Normalized values:")
for num in nums:
    normalized = (num - min_val) / (max_val - min_val)
    print(f"{normalized:.2f}")