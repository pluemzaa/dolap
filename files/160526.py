nums = input('Enter a series of numbers separated by commas: ')
nums = nums.split(',')
n = len(nums)
s = 0
for i in range(n): 
    nums[i] = float(nums[i])
    
mx = max(nums)
mn = min(nums)
print('Normalized values:')
for i in range(n): 
    s = (nums[i] - mn) / (mx - mn)
    print(f'{s:.2f}')