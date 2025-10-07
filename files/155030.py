nums1 = input("Enter a series of numbers separated by commas: ")
nums = nums1.split(",")
nums[0] = int(nums[0])
nums[1] = int(nums[1])
nums[2] = int(nums[2])
nums[3] = int(nums[3])
nums[4] = int(nums[4])
x_max = max(nums)
x0 = nums[0] is x_max
x1 = nums[1] is x_max
x2 = nums[2] is x_max
x3 = nums[3] is x_max
x4 = nums[4] is x_max
print(f"{nums[0]} is the maximum value:",x0)
print(f"{nums[1]} is the maximum value:",x1)
print(f"{nums[2]} is the maximum value:",x2)
print(f"{nums[3]} is the maximum value:",x3)
print(f"{nums[4]} is the maximum value:",x4)