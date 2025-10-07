nums = input("Enter a series of numbers separated by commas: ").split(",")
i = 0
for i in range(len(nums)):
    nums[i] = int(nums[i])
    
Max = nums[0]
print('Normalized values:')
for i in range(len(nums)):
    print(f'{((nums[i] - min(nums))/(max(nums)-min(nums))):.2f}')