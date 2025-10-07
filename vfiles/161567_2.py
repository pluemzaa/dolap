nums = input('Enter number: ')
nums = int(nums)

if nums < 1:
    print('Erorr number must be 1 or greater')
else:
    for i in range(1,nums+1):
        a = '*' * (2*i)
        print(a)
        print(a)