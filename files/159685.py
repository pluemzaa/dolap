v = int(input("Please enter vehicle type (1: Motorcycle, 2: Personal Car): "))
h = float(input("Please enter the number of parking hours: "))

if v == 1 or v == 2:
    if h > 0:
        if h < 1:
            fee = 0
        elif v == 1:
            fee = 10 + (h - 1) * 5
        elif v == 2:
            fee = 30 + (h - 1) * 15
        print(f"Parking fee: {fee:.2f} THB")
    else:
        print("Please enter a valid number of parking hours")
else:
    print("Invalid vehicle type")