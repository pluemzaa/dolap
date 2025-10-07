nums = input("Enter a series of numbers separated by commas:")
nums = nums.split(",")

for i in range(len(nums)):
    nums[i] = int(nums[i])
    
max_nums = max(nums)
min_nums = min(nums)
print("Normalized values:")

for i in range(len(nums)):
    nf = (nums[i] - min_nums)/(max_nums - min_nums)
    print("%.2f" %nf)