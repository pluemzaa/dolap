nums = input("Enter a series of numbers separated by commas: ")
nums = nums.split(",")

_min = int(min(nums))
_max = int(max(nums))

i = 0
print("Normalized values: ")
for i in range(len(nums)):
    nums[i] = int(nums[i])
    x_scaled = (nums[i]-_min)/(_max - _min)
    i += 1
    
print("%.2f"%x_scaled)