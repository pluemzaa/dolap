c = 0
total = 0
i = float(input("Enter a number (enter 0 to stop):"))
while i != 0:
    total = total + i
    i = float(input("Enter a number (enter 0 to stop):"))
    c = c+1

if c == 0:
    print("No numbers entered.")
else:
    a = total/c
    print("Average:",a)