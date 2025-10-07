nums = input("Enter a series of numbers separated by commas: ").split(',')

for i in range(len(nums)):
    nums[i] = int(nums[i])

max = max(nums)
min = min(nums)

print("Normalized values:")

for i in range(len(nums)):
    x_norm = (nums[i] - min) / (max - min)
    print(f"{x_norm:.2f}")