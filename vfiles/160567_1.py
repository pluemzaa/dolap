nums = input("Enter a series of numbers separated by commas: ")
nums = nums.split(",")

for i in range(0,len(nums)):
    nums[i] = int(nums[i])

_max = max(nums)
_min = min(nums)

print("Normalized values:")
for i in range(len(nums)):
    x_scaled = (nums[i]-min(nums))/(max(nums)-min(nums))
    print(f"{x_scaled:.2f}")