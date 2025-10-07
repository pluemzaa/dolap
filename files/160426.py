num = input('Enter a series of numbers separated by commas: ')
num = num.split(",")
for i in range(0,len(num)):
    num[i] = int(num[i])
print('Normalized values:')
for i in range(0,len(num)):
    re = ( num[i] - min(num) ) / (max(num) - min(num))

    print(f"{re :.2f}")