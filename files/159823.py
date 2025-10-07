sum = 0
aver = 0
num = int(input("Enter a number (enter 0 to stop):"))

while num != 0 :
    sum = sum + num
    aver = aver + 1
    num = int(input("Enter a number (enter 0 to stop):"))
if aver > 0 :
    average = sum / aver
    print("Average:",average)
else :
    print("No numbers entered.")