total = 0
total = 0.0
count = 0
num = int(input("Enter a number (enter 0 to stop): ")) and float(input("Enter a number (enter 0 to stop): "))
while num != 0 :
  total += num
  count += 1
  num = int(input("Enter a number (enter 0 to stop): ")) and float(input("Enter a number (enter 0 to stop): "))
  average = total / count
if num != 0 :
  print("Average:", average)
else :
  print("No numbers entered.")