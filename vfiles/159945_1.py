sum = 0
i = 0
num = int(input("Enter a number (enter 0 to stop):"))
while num !=0:
    sum+=num
    i+=1
    num = int(input("Enter a number (enter 0 to stop):"))
if i > 0:
    avg = sum / i
    print('Average:',avg)
else:
    print('No numbers entered.')