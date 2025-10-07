total = 0
count = 0
number = float(input("Enter a number (enter 0 to stop):"))
while number != 0:
    total += number
    count += 1
    number = float(input("Enter a number (enter 0 to stop):"))
if count == 0:
    print("No numbers entered.")
else:
    print("Average:", total / count)