nums = input("Enter a series of numbers separated by commas: ").split(',')

for i in range(len(nums)):
    nums[i] = int(nums[i])

Min = min(nums)
Max = max(nums)

print("Normalized values:")
for i in range(len(nums)):
     x = nums[i]
     x_scaled = (x - Min) / (Max - Min)
     print(f"{x_scaled:.2f}")