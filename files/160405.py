nums = input("Enter a series of numbers separated by commas:")
nums = nums.split(",")

for i in range(0,len(nums)):
    nums[i] = int(nums[i])

num_min = min(nums)
num_max = max(nums)
print("Normalized values:")

for i in nums:
    
    print(f"{(i-num_min)/(num_max-num_min):.2f}")