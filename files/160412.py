nums = input("Enter a series of numbers separated by commas: ")
nums = nums.split(",")
for i in range(0,len(nums)):
    nums[i] = int(nums[i])

max_ = nums[0]
for i in range(len(nums)):
    if nums[i] > max_:
        max_ = nums[i]
        print("set the maximum value to ",max_)
    continue
print("The maximum value is ",max_)