c = 0
t = 0
while True:
    num = int(input("Enter a number (enter 0 to stop): "))
    if num == 0:
        break
    t += num
    c += 1
if c == 0:
    print("No numbers entered.")
else:
    average = t / c
    print("Average:", average)