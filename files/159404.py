vehicle_type = int(input("Please enter vehicle type (1: Motorcycle, 2: Personal Car): "))
hours = float(input("Please enter the number of parking hours: "))
if vehicle_type == 1 or vehicle_type == 2:
    if hours <= 0:
        print("Please enter a valid number of parking hours")
    else:
        if hours < 1:
            fee = 0.00
        else:
            if vehicle_type == 1:
                fee = 10 + (hours - 1) * 5
            else:
                fee = 30 + (hours - 1) * 15
        print("Parking fee: %.2f THB" % fee)
else:
    print("Invalid vehicle type")