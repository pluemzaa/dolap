nums = input("Enter a series of numbers separated by commas: ")
nums = nums.split(",")

for i in range(0,len(nums)):
    nums[i] = int(nums[i])

a = min(nums)
s = max(nums)
tm = 0
print("Normalized values:")
for i in range(0,len(nums)):
    tm = (nums[i]-a)/(s-a)
    print(f"{tm}")