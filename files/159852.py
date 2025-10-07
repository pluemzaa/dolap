a = float(input("Enter a number (enter 0 to stop): "))
sum = 0
count = 0
if a == 0:
    print("No numbers entered")
else:
    while a != 0:
        sum += a
        count += 1
        a = float(input("Enter a number (enter 0 to stop): "))
    avg = sum/count
    print(f"Average: {avg}")