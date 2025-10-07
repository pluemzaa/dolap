nums = input('Enter a series of numbers separated by commas:')
nums = nums.split(",")

for i in range(len(nums)):
    nums[i] = int(nums[i])
       
maxx = nums[0]
for i in range(len(nums)):
    if nums[i] > maxx:
        maxx = nums[i]
minn = nums[0]
for i in range(len(nums)):
    if nums[i] < minn:
        minn = nums[i]
for i in range(len(nums)):
    x_sclad = (nums[i]-minn)/(maxx-minn)
    print('Normalized values:',end=(""))
    print(f'{x_sclad:.2f}',sep=("\n"))