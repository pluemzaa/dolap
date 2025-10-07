nums = input('Enter number: ')
nums = int(nums)
for i in range(nums):
    for j in range(i+1):
        print('**')
        print('**',end = '')
    print()