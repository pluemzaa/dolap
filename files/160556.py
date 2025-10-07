nums = input("Enter numbers separated by commas: ")
nums = nums.split(",")
x = input("Enter number to search: ")

found = False 

for i in range(len(nums)):
    if x == nums[i]:
        print('Found', x, 'at index', i)
        found = True
        

if not found:
    print("No", x, "found.")