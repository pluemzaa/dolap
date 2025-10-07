n=1;x = 0;s = 0
while True:
    n = int(input("Enter a number (enter 0 to stop):"))
    if n != 0:
        s += n ; x += 1
    else:
        break
if x == 0:
    print("No numbers entered.")
elif x != 0 :
    print("Average:", s / x)