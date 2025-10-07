cal = 0
total = 0

while True:
    num = float(input("Enter a number (enter 0 to stop): "))
    if num == 0:
        break
    total += num
    cal += 1

if cal > 0:
    average = total / cal
    print("Average:", average)
else:
    print("No numbers entered.")