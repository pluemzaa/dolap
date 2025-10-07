#Lab5 ข้อ1
total = 0
count = 0

i = float(input("Enter a number (enter 0 to stop): "))
while i != 0:
    total += i
    count += 1
    i = float(input("Enter a number (enter 0 to stop): "))

if count == 0:
    print("No numbers entered.")
else:
    print("Average:", total / count)