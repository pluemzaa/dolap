total = 0
x = int(input('Enter a number (enter 0 to stop):'))
while x != 0:
   total += x
   x = int(input('Enter a number (enter 0 to stop):'))
   average = total//3
print(average)