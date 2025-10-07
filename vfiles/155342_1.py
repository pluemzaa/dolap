nums_text = "20,10,30,50"
nums = nums_text.split(",")
nums[0] = int(nums[0])
nums[1] = int(nums[1])
nums[2] = int(nums[2])
nums[3] = int(nums[3])
min_x = min(nums)
max_x = max(nums)
print(min_x,min_x)
r0 = nums[0]-min_x
r1 = nums[1]-min_x
r2 = nums[2]-min_x
r3 = nums[3]-min_x
print("%.2f" %r0)
print("%.2f" %r1)
print("%.2f" %r2)
print("%.2f" %r3)