nums = input("Enter a series of numbers separated by commas:\n")
nums = nums.split(",")
nums_max = max(nums)
nums_min = min(nums)
for i in range(len(nums)):
    nums[i] = int(nums[i])
    nums_min = float(nums_min)
    nums_max = float(nums_max)
x = 0
print("Normalized values:")
for i in range(len(nums)):
    x = (nums[i] - nums_min)/(nums_max - nums_min)
    print("%.2f"%(x))