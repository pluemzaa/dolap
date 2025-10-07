total = 0
count = 0
num = int(input("Enter a number (enter 0 to stop): "))
while num != 0 :
  total += num
  count += 1
  num = int(input("Enter a number (enter 0 to stop): "))
  average = total / count
print("Average:", average)