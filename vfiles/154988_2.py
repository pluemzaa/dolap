nums_text =int(input ('Enter a series of numbers separated by commas: '))
nums = nums_text.split(",")

nums[0] = int(nums[0])
nums[1] = int(nums[1])
nums[2] = int(nums[2])
nums[3] = int(nums[3])
nums[4] = int(nums[4])

nums = [10,20,30,40,50] 
x_min = min(nums)
x_max = max(nums)
print(x_min,x_max)

r0 = nums[0] - x_min/x_max-x_min
r1 = nums[1] - x_min/x_max-x_min
r2 = nums[2] - x_min/x_max-x_min
r3 = nums[3] - x_min/x_max-x_min
r4 = nums[4] - x_min/x_max-x_min
print("Normalized values: ","%.2f" % r0)
print("Normalized values: ","%.2f" % r1)
print("Normalized values:","%.2f" % r2)
print("Normalized values:","%.2f" % r3)
print("Normalized values:","%.2f" % r4)