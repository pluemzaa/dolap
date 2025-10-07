nums = input("Enter a series of numbers separated by commas:")
nums = nums.split(",")
nums = [float(x) for x in nums] 

_min = min(nums)
_max = max(nums)

print("Normalized values:")
if _max == _min:
    for _ in nums:
        print("0.00")
else:
    for x in nums:
        n = (x - _min) / (_max - _min)
        print(f"{n:.2f}")