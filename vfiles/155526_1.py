nums_text = input("Enter a series of numbers separated by commas: ")

nums = nums_text.split(",")
nums[0] = int(nums[0])
nums[1] = int(nums[1])
nums[2] = int(nums[2])
nums[3] = int(nums[3])
nums[4] = int(nums[4])

x1 = min(nums)
x2 = max(nums)


x_s1 = (nums[0]-x1)/(x2-x1)
x_s2 = (nums[1]-x1)/(x2-x1)
x_s3 = (nums[2]-x1)/(x2-x1)
x_s4 = (nums[3]-x1)/(x2-x1)
x_s5 = (nums[4]-x1)/(x2-x1)
print("Normalized values",end=('\n'))
print("%.2f"%x_s1,"%.2f"%x_s2,"%.2f"%x_s3,"%.2f"%x_s4,"%.2f"%x_s5,sep=('\n'))