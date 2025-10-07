num = input("Enter a series of numbers separated by commas: ")

nums = num.split(',')
numbers = [0] * len(nums)

for i in range(len(nums)):
    numbers[i] = float(nums[i])


min_val = min(numbers)
max_val = max(numbers)


normalized = [0] * len(numbers)

for i in range(len(numbers)):
    normalized[i] = (numbers[i] - min_val) / (max_val - min_val)


print("Normalized values:")
for i in range(len(normalized)):
    print(f"{normalized[i]:.2f}")