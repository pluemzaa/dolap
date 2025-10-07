nums = input("Enter a series of numbers separated by commas: ").split(",")
for i in range(5):
    nums[i] = int(nums[i])

maxNum = max(nums)
for num in nums:
    print(num, "is the maximum value:", num == maxNum)