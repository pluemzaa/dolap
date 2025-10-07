a = input("Enter a series of numbers separated by commas: ")
nums = a.split(",")

for i in range (len(nums)):
    nums[i] = float(nums[i])

_min=min(nums)
_max=max(nums)

print("Normalized values:")
for num in nums:
    if _max == _min:
        normalized = 0.0
    else :
        normalized = (num - _min)/(_max - _min)
    print("{:.2f}".format(normalized))