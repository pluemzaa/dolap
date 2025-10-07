nums = input("Enter numbers separated by commas: ").split(",")
y = int(input("Enter number to search: "))

for i in range(len(nums)):
     nums[i] = int(nums[i])

for i in range(0,len(nums)):    
    if y == nums[i]:
        print('Found',y,'at index', i)

if y != nums[i]:
    print('No',y,'found.')