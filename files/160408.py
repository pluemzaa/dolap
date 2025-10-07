nums = input("Enter a series of numbers separated by commas: ")
nums = nums.split(",")

for i in range(0,len(nums)):
    nums[i] = int(nums[i])


_max = nums[0]
for j in range(0,len(nums)):
    if nums[j] > _max:
        _max = nums[j]

_min = nums[0]
for k in range(0,len(nums)):
    if nums[k] < _min:
        _min = nums[k] 
print("Normalized values:")
for l in range(0,len(nums)):
    nums[l] = (nums[l] - _min)/(_max-_min)
    print(f"{nums[l]:.2f}")