nums = input("Enter numbers separated by commas:")
nums = nums.split(",")
nums_s = int(input("Enter number to search:"))
f = False
for i in range(0,len(nums)):
    nums[i] = int(nums[i])
for i in range(0,len(nums)):
    if nums_s== nums[i]:
        print("Found", nums_s, "at index",i)
        f = True
if f == False:
    print("No", nums_s, "found.")