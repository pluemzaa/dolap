nums_text = input("Enter a series of numbers separated by commas:")
nums =nums_text.split(",")
nums[0] = int(nums[0])
nums[1] = int(nums[1])
nums[2] = int(nums[2])
nums[3] = int(nums[3])
nums[4] = int(nums[4])



x1 = min(nums)
x2 = max(nums)

x_scaled = (nums[0]-x1)/(x2-x1)
x_scaled1 = (nums[1]-x1)/(x2-x1)
x_scaled2 = (nums[2]-x1)/(x2-x1)
x_scaled3 = (nums[3]-x1)/(x2-x1)
x_scaled4 = (nums[4]-x1)/(x2-x1)
print("Normalized values:",end=('\n'))
print("%.2f"% x_scaled,"%.2f"% x_scaled1,"%.2f"% x_scaled2,"%.2f"% x_scaled3,"%.2f"% x_scaled4,sep=('\n'))