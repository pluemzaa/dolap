nums = input('Enter numbers separated by commas: ')
snum = input('Enter number to search: ')
nums = nums.split(',')
i = snum
#cast str -> int
nums[0] = int(nums[0])
nums[1] = int(nums[1])
nums[2] = int(nums[2])
nums[3] = int(nums[3])

for i in range(len(nums)):
    if i==nums[i]:
        print('Found ',snum,'at index : ',snum)
        break
else:
    print('No zero found.')