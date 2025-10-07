Xsum = 0
nums = input("Enter a series of numbers separated by commas: ")
nums = nums.split(",")
for i in range(len(nums)):
    nums[i] = int(nums[i])

_max = nums[0]
for i in range(len(nums)):
    if nums[i] > _max:
        _max = nums[i]

_min = nums[0]
for i in range(len(nums)):
    if nums[i] < _min:
        _min = nums[i]
print("Normalized values:")
for i in range(len(nums)):
    Xsum = (nums[i] - _min)/(_max - _min)
    print(f"{Xsum:.2f}")