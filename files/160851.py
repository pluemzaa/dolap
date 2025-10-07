nums = input("Enter a series of numbers separated by commas: ")
nums = nums.split(",")
n = len(nums)
for i in range(n):
    nums[i]= int(nums[i])    
_min = min(nums)
_max = max(nums)
print('Normalized values:')
for i in range(n):
    avg = (nums[i])-_min
    i = 0+1
    s = _max-_min
    sd = avg/s
    print(f'{sd:.2f}')