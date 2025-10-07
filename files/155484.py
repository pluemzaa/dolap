x = input("Enter a series of numbers separated by commas: ")
nums = x.split(",")
nums[0] = int(nums[0])
nums[1] = int(nums[1])
nums[2] = int(nums[2])
nums[3] = int(nums[3])
nums[4] = int(nums[4])


x_max = max(nums)
r0 = (x_max is nums[0])
r1 = (x_max is nums[1])
r2 = (x_max is nums[2])
r3 = (x_max is nums[3])
r4 = (x_max is nums[4])

#print(x_max in x)

print(nums[0],"is the maximum value:",r0)
print(nums[1],"is the maximum value:",r1)
print(nums[2],"is the maximum value:",r2)
print(nums[3],"is the maximum value:",r3)
print(nums[4],"is the maximum value:",r4)