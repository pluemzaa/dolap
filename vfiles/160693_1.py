count = 0
total = 0

while True:
    num = int(input("Enter a number (enter 0 to stop): "))
    if num == 0:
        break
    total += num
    count += 1

if count == 0:
    print("No numbers entered.")
else:
    average = total / count
    print("Average:", average)