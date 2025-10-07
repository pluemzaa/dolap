nums_str = input ("Enter a series of numbers separated by commas:")
nums = [float (x.strip()) for x in nums_str.split(",")]
min_x = min(nums)
max_x = max(nums)

print("Normalized values:")

r0 = (nums[0]-min_x) / (max_x-min_x)
r1 = (nums[1]-min_x) / (max_x-min_x)
r2 = (nums[2]-min_x) / (max_x-min_x)
r3 = (nums[3]-min_x) / (max_x-min_x)
r4 = (nums[4]-min_x) / (max_x-min_x)

print("%.2f" % r0)
print("%.2f" % r1)
print("%.2f" % r2)
print("%.2f" % r3)
print("%.2f" % r4)