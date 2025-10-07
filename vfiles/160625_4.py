nums = input("Enter a series of numbers separated by commas: ")
nums = nums.split(",")
n = len(nums)
for i in range(n):
    nums[i] = int(nums[i])

print("Normalized values:")

if max(nums) == min(nums):
    for i in range(n):
        print("0.00")
else:
    for i in range(n):
        avg = (nums[i] - min(nums)) / (max(nums) - min(nums))
        print("%.2f"%(avg))