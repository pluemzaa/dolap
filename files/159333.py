t = int(input("Please enter vehicle type (1: Motorcycle, 2: Personal Car): "))
hour = float(input("Please enter the number of parking hours: "))

if t == 1:
    if hour < 1 and hour >= 0:
        price = 0
        print(f"Parking fee: {price:.2f} THB")
    elif hour < 0:
        print(f"Please enter a valid number of parking hours")
    else:
        price = 10 + (hour - 1) * 5
        print(f"Parking fee: {price:.2f} THB")
elif t == 2:
    if hour < 1 and hour >= 0:
        price = 0
        print(f"Parking fee: {price:.2f} THB")
    elif hour < 0:
        print("Please enter a valid number of parking hours")
    else:
        price = 30 + (hour - 1) * 15
        print(f"Parking fee: {price:.2f} THB")
else:
    print("Invalid vehicle type")