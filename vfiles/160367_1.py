nums = input("Enter numbers separated by commas: ")
nums = nums.split(",")
numsearch = int(input("Enter number to search: "))

for i in range(0,len(nums)):
    nums[i] = int(nums[i])

for i in range(0,len(nums)):
    if numsearch == nums[i]:
        print("Found",numsearch,"at index",i)
    else:
        print("No",numsearch,"found.")