vehicle_type = int(input("Please enter vehicle type (1: Motorcycle, 2: Personal Car): "))
hours = float(input("Please enter the number of parking hours: "))
if vehicle_type == 1:
    if hours <= 0:
        print("Please enter a valid number of parking hours")
    elif hours < 1:
        print("Free")
    else:
        if hours <= 1:
            parking_fee = 10 * hours
        else:
            parking_fee = 10 + (hours - 1) * 5

        print(f"Parking fee: {parking_fee:.2f} THB")
elif vehicle_type == 2:
    if hours <= 0:
        print("Please enter a valid number of parking hours")
    elif hours < 1:
        print("Free")
    else:
        if hours <= 1:
            parking_fee = 30 * hours
        else:
            parking_fee = 30 + (hours - 1) * 15

        print(f"Parking fee: {parking_fee:.2f} THB")
else:  
    print("Invalid vehicle type")