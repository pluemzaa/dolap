num = input('Enter a series of numbers separated by commas: ')
num = num.split(",")

for i in range(0,len(num)):
    num[i] = int(num[i])
    
_max = num[0]
for i in range(len(num)):
    if num[i] > _max:
        _max = num[i]
        print("set the maximum value to ", _max)
        
print('The maximum value is ', _max)