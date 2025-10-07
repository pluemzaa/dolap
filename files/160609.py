vehicle_type = int(input("Please enter vehicle type (1: Motorcycle, 2: Personal Car): "))
hours = int(input("Please enter the number of parking hours: "))

if vehicle_type not in [1, 2]:
    print("Invalid vehicle type")
elif hours < 0:
    print("Please enter a valid number of parking hours")
elif hours < 1:
    print("Parking is free")
else:
    if vehicle_type == 1:  # Motorcycle
        if hours == 1:
            fee = 10
        else:
            fee = 10 + (hours - 1) * 5
    elif vehicle_type == 2:  # Personal Car
        if hours == 1:
            fee = 30
        else:
            fee = 30 + (hours - 1) * 15
    print("Parking fee is:", fee, "Baht")