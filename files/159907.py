n = int(input('Enter a number (enter 0 to stop):'))
i = 1
total = 0
if n!=0:
    while n != 0:
        total = (total+n)/i
        i = i+1
        n = int(input('Enter a number (enter 0 to stop):'))
    print('Average:',total)
else:
    print('No numbers entered.')