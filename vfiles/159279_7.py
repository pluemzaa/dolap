v = float(input("Please enter vehicle type (1: Motorcycle, 2: Personal Car): "))
h = float(input("Please enter the number of parking hours: "))
if v == 1:
    if h < 0:
        print("Please enter a valid number of parking hours")
    elif h < 1:
        print(f"Parking fee: {h * 0:.2f} THB")
    elif h == 1:
        print(f"Parking fee: {h * 10:.2f} THB")
    elif h > 1:
        print(f"Parking fee: {(h * 10)/2:.2f} THB")
elif v == 2:
    if h < 0:
        print("Please enter a valid number of parking hours")
    elif h < 1:
        print(f"Parking fee: {h * 0:.2f} THB")
    elif h == 1:
        print(f"Parking fee: {h * 30:.2f} THB")
    elif h > 1:
        print(f"Parking fee: {(h * 30)/2:.2f} THB")
else:
    print("Invalid vehicle type")