vehicle_type = int(input("Please enter vehicle type (1: Motorcycle, 2: Personal Car): "))
parking_hours = float(input("Please enter the number of parking hours: "))

if vehicle_type not in [1, 2]:
    print("Invalid vehicle type")
elif parking_hours <= 0:
    print("Please enter a valid number of parking hours")
else:
    if parking_hours < 1:
        fee = 0.00
    else:
        first_hour = 1
        additional_hours = parking_hours - 1

        if vehicle_type == 1:
            fee = (first_hour * 10) + (additional_hours * 5)
        elif vehicle_type == 2:
            fee = (first_hour * 30) + (additional_hours * 15)

    print(f"Parking fee: {fee:.2f} THB")