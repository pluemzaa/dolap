num = input("Enter a series of numbers separated by commas: ")
num = num.split(',')
x = 0
for i in range(len(num)):
    num[i] = int(num[i])
_max = max(num)
_min = min(num)
print("Normalized values: ")
for i in range(len(num)):
    x = (num[i] - _min)/(_max - _min)
    print('%.2f'%x)