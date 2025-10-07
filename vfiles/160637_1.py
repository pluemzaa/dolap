n = int(input("Enter a number (enter 0 to stop): "))
sum = 0
all_num = []
while n != 0:
    if n == 0:
        print("No numbers entered.")
    all_num.append(n)
    n = int(input("Enter a number (enter 0 to stop): "))
for i in all_num:
    sum = sum + i
average = sum / len(all_num)
print(average)