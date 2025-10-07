nums=input('Enter a series of numbers separated by commas: ')

nums_text=nums
nums=nums_text.split(',')
r0=nums[0]=int(nums[0])
r1=nums[1]=int(nums[1])
r2=nums[2]=int(nums[2])
r3=nums[3]=int(nums[3])
r4=nums[4]=int(nums[4])

_max=max(nums)

print(f'{r0} is the maximum value: {r0 is _max}')
print(f'{r1} is the maximum value: {r1 is _max}')
print(f'{r2} is the maximum value: {r2 is _max}')
print(f'{r3} is the maximum value: {r3 is _max}')
print(f'{r4} is the maximum value: {r4 is _max}')