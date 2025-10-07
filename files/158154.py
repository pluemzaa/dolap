n = int(input('Enter a number (enter 0 to stop):'))
avg = 0
while n != 0 :
    n = int(input('Enter a number (enter 0 to stop):'))
    avg = avg + n

if avg == 0:
    print('No numbers entered.')
else:
    print('Average:',float(avg))