nums_text = input("Enter a series of numbers separated by commas: ")
nums = nums_text.split(",")
nums [0] = int(nums[0])
nums [1] = int(nums[1])
nums [2] = int(nums[2])
nums [3] = int(nums[3])
nums [4] = int(nums[4])
# nums = nums_text
x=10

# result = [90,0,10,40]
_min = min(nums)
_max = max(nums)
print("Normalized values:")
r0 = (nums[0]-min(nums))/(max(nums)-min(nums))
r1 = (nums[1]-min(nums))/(max(nums)-min(nums))
r2 = (nums[2]-min(nums))/(max(nums)-min(nums))
r3 = (nums[3]-min(nums))/(max(nums)-min(nums))
r4 = (nums[4]-min(nums))/(max(nums)-min(nums))

print("%.2f" % r0)
print("%.2f" % r1)
print("%.2f" % r2)
print("%.2f" % r3)
print("%.2f" % r4)