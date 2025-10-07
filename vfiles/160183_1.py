nums = input("Enter numbers separated by commas: ")
nums = nums.split(",")
y = int(input("Enter number to search: "))
#cast
i = 0
for i in range(len(nums)):
    nums[i] = int(nums[i])
    i += 1
i = 0
for i in range(len(nums)):
    if y == nums[i]:
        print("Found", y , "at index",i)
        break
    i += 1
else:
    print("No",y,"found.")