nums = input("Enter a series of numbers separated by commas:")
nums = nums.split(",")

n = len(nums)
for i in range(n):
    nums[i] = int(nums[i])


_min = min(nums)
_max = max(nums)


_min = int(_min)
_max = int(_max)




print("Normalized values:")
for i in range(n):
    x_bar = ((nums[i] - _min)) / ((_max) - (_min))
    print(f"{x_bar:.2f}")