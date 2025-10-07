n1 = input("Enter a series of numbers separated by commas:")
n1 = n1.split(',')

for i in range(len(n1)):
    n1[i] = int(n1[i])

_max = n1[0]
for i in range(len(n1)):
    if n1[i] > _max :
        _max = n1[i]
        print('set the maximum value to',_max)

print('The maximum value is',_max)