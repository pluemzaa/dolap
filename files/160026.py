print("Input:")
total = 0
count = 0

while True:
    num = int(input("Enter a number (enter 0 to stop): "))
    if num == 0:
        break
    total += num
    count += 1

print("Output:")
if count == 0:
    print("No numbers entered.")
else:
    average = total / count
    print(f"Average: {average}")