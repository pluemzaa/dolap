x = 0
sum = 0
while True:
    num = int(input("Enter a number (enter 0 to stop):"))
    if num == 0:
        break
    sum += 1
    x += num
if sum == 0:
    print("No numbers entered.")
else:
    print(x/sum)