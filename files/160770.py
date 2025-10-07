count = 0
total = 0

while True:
    number = int(input("Enter a number (enter 0 to stop): "))
    if number == 0:
        break
    total += number
    count += 1
if count == 0:
    print("No numbers entered.")
else:
    average = total / count
    print("Average:", average)