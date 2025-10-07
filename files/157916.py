count = 0
total = 0.0  # ใช้ float เพราะมีทศนิยม

while True:
    num = float(input("Enter a number (enter 0 to stop): "))
    if num == 0:
        break
    total += num
    count += 1

if count == 0:
    print("No numbers entered.")
else:
    average = total / count
    print("Average:", average)