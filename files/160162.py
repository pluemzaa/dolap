nums = input("Enter numbers separated by commas:")
nums = nums.split(",")
for i in range (len(nums)):
    nums[i] = int(nums[i])

y = int(input("Enter number to search: "))
found = False
for i in range (len(nums)):
  if nums[i]==y:
        print("Found", y , "at index" ,i)
        found = True
if not found:
    print('No', y , "found.")