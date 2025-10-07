y = 0
z = 0
while True:
    x = int(input("Enter a number (enter 0 to stop): "))
    if x == 0:
        break
    y += x
    z += 1
if z == 0:
    print("No numbers entered.")
else:
    av= y / z
    print("Average:", av)