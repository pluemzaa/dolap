def calculate_parking_fee():
    """
    Calculates the parking fee based on vehicle type and parking hours.
    """
    try:
        vehicle_type = int(input("Please enter vehicle type (1: Motorcycle, 2: Personal Car): "))
    except ValueError:
        print("Invalid vehicle type")
        return

    if vehicle_type not in [1, 2]:
        print("Invalid vehicle type")
        return

    try:
        parking_hours = float(input("Please enter the number of parking hours: "))
    except ValueError:
        print("Please enter a valid number of parking hours")
        return

    if parking_hours <= 0:
        print("Please enter a valid number of parking hours")
        return

    parking_fee = 0.0

    if parking_hours < 1:
        parking_fee = 0.0
    else:
        if vehicle_type == 1:  # Motorcycle
            parking_fee = 10.0 + (max(0, parking_hours - 1) * 5.0)
        elif vehicle_type == 2:  # Personal Car
            parking_fee = 30.0 + (max(0, parking_hours - 1) * 15.0)

    print(f"Parking fee: {parking_fee:.2f} THB")

# Run the program
calculate_parking_fee()