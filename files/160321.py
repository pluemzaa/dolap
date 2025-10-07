nums = input("Enter a series of numbers separated by commas: ")
nums = nums.split(",")

print("Normalized values:")

for i in range(len(nums)):
    nums[i] = int(nums[i])

_min = min(nums)
_max = max(nums)
for i in range(len(nums)):
    x = nums[i]
    _x = (x-_min)/(_max-_min)
    print(f"{_x:.2f}")