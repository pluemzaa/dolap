x = int(input("Please enter vehicle type (1: Motorcycle, 2: Personal Car): "))
y = float(input("Please enter the number of parking hours: "))

if x not in [1, 2]:
    print("Invalid vehicle type")
elif y < 0:
    print("Please enter a valid number of parking hours")
else:
    z = 0.0
    if y < 1:
        z = 0.0
    else:
        if x == 1:
            z = 10 + (y -1 ) * 5
        elif x == 2:
            z = 30 + (y - 1) * 15 
print(f"Parking fee: {z:.2f}THB")