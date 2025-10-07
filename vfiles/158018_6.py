count = 0
total = 0

while True:
    num = int(input("Enter a number (enter 0 to stop): "))
    if num == 0:
        break
    count += 1
    total += num

if count == 0:
    print("No numbers entered.")
else:
    result = total / count
    print("Average:", result)