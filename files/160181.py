nums = input("Enter numbers separated by commas: ")
search = int(input('Enter number to search: '))
nums = nums.split(",")
i = 0

for i in range(len(nums)):
    nums[i] = int(nums[i])
    
for i in range(len(nums)):
    if search == nums[i]:
        print(f'Found {search} at index{i}')

if search not in nums:
    print(f'No {search} found.')