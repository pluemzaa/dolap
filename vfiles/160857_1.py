total = 0
number = float(input("Enter a number (enter 0 to stop): "))
while number != 0:
  total = total + number
  number = float(input("Enter a number (enter 0 to stop): "))
x = float(total)
avg = x / int(len(str(x)))
if avg ==0:
    print("No numbers entered.")
else:
    print("Average:", float(avg))