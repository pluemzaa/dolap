nums = input("Enter a series of numbers separated by commas: ")
nums = nums.split(",")

for i in range(len(nums)):
    nums[i] = float(nums[i])

_max = max(nums)
_min = min(nums)

if _max == _min:
    print("Normalized values:")
    print(0.00)
else:
    scaled = [(a - _min) / (_max - _min) for a in nums]
    print("Normalized values:")
    for n in scaled:
        print(f"{n:.2f}")