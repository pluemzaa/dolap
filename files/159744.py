vehicle_type = input ("Please enter vehicle type (1: Motorcycle, 2: Personal Car): ")
try:
    hours = float(input("Please enter the number of parking hours: "))

    if hours <= 0:
       print("Please enter a valid number of parking hours")
    elif vehicle_type not in ['1', '2']:
        print("Invalid vehicle type")
    else:
        if hours < 1:
            fee = 0.0
        else:
            if vehicle_type == '1':
                fee = 10 + (hours - 1) * 5
            else:
                fee = 30 + (hours - 1) * 15
    print(f"Parking fee: {fee:.2f} THB")
except ValueError:
    print("Please enter a valid number of parking hours")
except ValueError:
    print("Please enter a valid number of parking hours")