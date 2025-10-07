sum = 0
number = int(input("Enter a number (enter 0 to stop): "))
while number != 0 :
    number = int(input("Enter a number (enter 0 to stop): "))
    sum = sum + number
if sum == 0 :
    print("No numbers entered.")
else :
    print(sum)