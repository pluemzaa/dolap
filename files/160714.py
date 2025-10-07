nums = input("Enter a series of numbers separated by commas:")
nums = nums.split(",")
for i in range(len(nums)):
    nums[i] = float(nums[i])
nums_min = min(nums)
nums_max = max(nums)
print("Normalized values:")
for i in nums:
    print(f"{(i - nums_min) / (nums_max - nums_min):.2f}")