vt = float(input("Please enter vehicle type (1: Motorcycle, 2: Personal Car): "))
h = float(input("Please enter the number of parking hours: "))

if vt == 1:
    if h >= 1:
        price = 10 + (h - 1) * 5
        print(f"Parking fee: {price:.2f} THB")
    elif h > 0:
        print("Parking fee: 0.00 THB")
    else:
        print("Please enter a valid number of parking hours")

elif vt == 2:
    if h >= 1:
        price = 30 + (h - 1) * 15
        print(f"Parking fee: {price:.2f} THB")
    elif h > 0:
        print("Parking fee: 0.00 THB")
    else:
        print("Please enter a valid number of parking hours")

else:
    print("Invalid vehicle type")