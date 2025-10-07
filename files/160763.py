text = input("Enter a series of numbers separated by commas:")

nums = [float(x) for x in text.split(",")]

_min = min(nums)
_max = max(nums)

total = [(x - _min) / (_max - _min) for x in nums]

print("Normalized values:")
for n in total:
    print(f"{n:.2f}")