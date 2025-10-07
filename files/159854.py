total = 0
i = 0
number = int(input("Enter a number (enter 0 to stop):"))
while number != 0:
    total += number
    i = i+1
    number = int(input("Enter a number (enter 0 to stop):"))
sum1 = total / i
print("Average:", sum1)