total = 0
count = 0
num = 1

while num != 0:
    num = float(input("Enter a number (enter 0 to stop): "))
    if num != 0:
        total = total + num
        count = count + 1

if count > 0:
    print("Average:", total / count)
else:
    print("No numbers entered.")