vehicle_type = input("Please enter vehicle type (1: Motorcycle, 2: Personal Car): ")
hours_input = input("Please enter the number of parking hours: ")

if vehicle_type not in ["1", "2"]:
    print("Invalid vehicle type")
else:
    try:
        hours = float(hours_input)
    except ValueError:
        print("Please enter a valid number of parking hours")
        exit()
    if hours <= 0:
        print("Please enter a valid number of parking hours")
    else:
        if hours < 1:
            fee = 0.00
        elif vehicle_type == "1":
            fee = 10 + (hours - 1) * 5
        elif vehicle_type == "2":
            fee = 30 + (hours - 1) * 15
        print(f"Parking fee: {fee:.2f} THB")