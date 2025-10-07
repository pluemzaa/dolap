nums = input("Enter a series of numbers separated by commas: ")
nums = nums.split(",")
for i in range (len(nums)):
    nums[i] = int(nums[i])
maxx = max(nums)
minx = min(nums)
print("Normalized values:")
for i in range(len(nums)):
    x = (nums[i]-minx)/(maxx-minx)
    print(f"{x:.2f}")