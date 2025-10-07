total=0
number = int(input("Enter a number (enter 0 to stop): "))
while number != 0:
  total += number
  number = int(input("Enter a number (enter 0 to stop): "))
x = float(total)
avg = x / int(len(str(x)))
if avg == 0:
  print('No numbers entered.')
else :
  print('Average:',float(avg))