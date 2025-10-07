nums = int(input('Enter number: '))
if nums < 1:
    print('Error number must be 1 or greater')
else:
    for i in range(1,nums+1):
        a = '*' * (2*i)
        print(a)
        print(a)