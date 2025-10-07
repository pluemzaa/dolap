totol = 0
count = 0
num = int(input("Enter a number (enter 0 to stop): "))
while num != 0 :
  totol += num
  count += 1
  num = int(input("Enter a number (enter 0 to stop): "))
if count != 0:
    average = totol / count
    print("Average:", average)
else:
    print("No numbers entered.")