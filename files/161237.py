nums = input("Enter a series of numbers separated by commas:")
nums = nums.split(",")

for i in range(len(nums)):
    nums[i] = int(nums[i]) 

xmin = min(nums)
xmax = max(nums)

print("Normalized values:")
for num in nums:
    x_scaled = (num - xmin) / (xmax- xmin)
    print(f"{x_scaled:.2f}")