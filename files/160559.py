nums = input("Enter numbers separated by commas:")
search = int(input("Enter number to search:"))
nums = nums.split(",")
i = 0

for i in range(len(nums)):
    nums[i] = int(nums[i])
    
found = False
for i in range(len(nums)):
    if search == nums[i]:
        print('Found', search ,'at index' , i)
        found = True
if not found:
    print("No ", search," found.")