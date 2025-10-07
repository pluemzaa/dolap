nums_text = input("Enter a series of numbers separated by commas:")
nums = nums_text.split(",")
nums[0] = int(nums[0])
nums[1] = int(nums[1])
nums[2] = int(nums[2])
nums[3] = int(nums[3])
nums[4] = int(nums[4])

min_x = min(nums)
max_x = max(nums)

x0 = nums[0]-min_x
x1 = nums[1]-min_x
x2 = nums[2]-min_x
x3 = nums[3]-min_x
x4 = nums[4]-min_x

under = max_x-min_x

r0 = x0/under
r1 = x1/under
r2 = x2/under
r3 = x3/under
r4 = x4/under

print("Normalized values: ")
print("%.2f" r0)
print("%.2f" r0)
print("%.2f" r0)
print("%.2f" r0)
print("%.2f" r0)