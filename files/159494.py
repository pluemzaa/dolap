v = float(input("Please enter vehicle type (1: Motorcycle, 2: Personal Car): "))
h = float(input("Please enter the number of parking hours: "))

price = 0
fprice = 0
if v == 1:
    if h < 0:
        print("Please enter a valid number of parking hours")
    if h == 1:
        print("Parking fee: 10.00 THB")
    elif h > 1:
        print(f"Parking fee: {10+((h-1)*5):.2f} THB")
    elif h < 1:
        print("Parking fee: 0.00 THB")
if v == 2:
    if h < 0:
        print("Please enter a valid number of parking hours")
    if h == 1:
        print("Parking fee: 30.00 THB")
    elif h > 1:
        print(f"Parking fee: {30+((h-1)*15):.2f} THB")
    elif h < 1:
        print("Parking fee: 0.00 THB")
else:
    print("Invalid vehicle type")