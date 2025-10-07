vehicle_type = int(input("Please enter vehicle type (1: Motorcycle, 2: Personal Car): "))

if vehicle_type not in [1, 2]:
    print("invalid vehicle type")
else:
    parking_hours = float(input("Please enter the number of parking hours: "))
    if parking_hours <= 0:
        print("Please enter a valid number of parking hours")
    else:
        if parking_hours < 1:
            fee = 0.00
        else:
            extra_hours = parking_hours - 1
            if vehicle_type == 1:
                fee = 10 + extra_hours * 5
            else:  # vehicle_type == 2
                fee = 30 + extra_hours * 15
        print(f"Parking fee: {fee:.2f} THB")