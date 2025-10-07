t = int(input("Please enter vehicle type (1: Motorcycle, 2: Personal Car): "))
h = float(input("Please enter the number of parking hours: "))

if t == 1 or t == 2:
    if h <= 0:
        print("Please enter a valid number of parking hours")
    elif h < 1:
        print("Parking fee: 0.00 THB")
    else:
        if t == 1:
            fee = 10 + (h - 1) * 5
        elif t == 2:
            fee = 30 + (h - 1) * 15
        print(f"Parking fee: {fee:.2f} THB")
else:
   print("Invalid vehicle type")