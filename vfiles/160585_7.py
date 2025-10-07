nums = input("Enter a series of numbers separated by commas:")
nums = nums.split(',')


n = len(nums)
_min= int(min(nums))
_max= int(max(nums))

for i in range(n):
    nums[i] = int(nums[i])

print("Normalized values:")

for i in range(n):
    x_bar = (nums[i] - (_min)) 
    x_bar= x_bar / ((_max) - (_min))
    print(f"{x_bar:.2f}")