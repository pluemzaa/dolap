nums = input("Enter a series of numbers separated by commas: ")

nums = nums.split(',')

nums[0] = int(nums[0])
nums[1] = int(nums[1])
nums[2] = int(nums[2])
nums[3] = int(nums[3])
nums[4] = int(nums[4])

min_x = min(nums)
max_x = max(nums)

xp0 = (nums[0] - min_x)/(max_x - min_x)
xp1 = (nums[1] - min_x)/(max_x - min_x)
xp2 = (nums[2] - min_x)/(max_x - min_x)
xp3 = (nums[3] - min_x)/(max_x - min_x)
xp4 = (nums[4] - min_x)/(max_x - min_x)

print(f"Normalized values: \n{xp0:.2f}\n{xp1:.2f}\n{xp2:.2f}\n{xp3:.2f}\n{xp4:.2f}")