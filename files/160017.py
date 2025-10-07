n = -1 
total = 0
c = 0
while n != 0:
    n = int(input("Enter a number (enter 0 to stop): "))
    if n != 0:
        total += n
        c += 1
if c > 0:
    a = total / c
    print("Average:",a)
else:
    print("No numbers entered.")