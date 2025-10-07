nums = input("Enter numbers separated by commas: ")
nums = nums.split(",")
k = input("Enter number to search: ")
k = int(k)

for i in range(0,len(nums)):
    nums[i] = int(nums[i])

for i in range(len(nums)):
    if  k == nums[i]:
        print("Found ",k," at index",i)
        continue
        # break
    elif k not in nums:
        print("No ",k," found.")
        break