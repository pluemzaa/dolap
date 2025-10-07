nums = input('Enter numbers separated by commas: ')
num = int(input('Enter number to search: '))
nums = nums.split(',')

for i in range(len(nums)): 
    nums[i] = int(nums[i])
    
for i in range(len(nums)):
    if num == nums[i]:
        print('Found',num,'at index ', i)
print('No',num,'found.')