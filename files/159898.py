total = 0      
count = 0     

while True:
    num = float(input("Enter a number (enter 0 to stop): "))
    if num == 0:
        break
    total += num
    count += 1

if count > 0:
    average = total / count
    print("Average:", average)
else:
    print("No numbers entered.")