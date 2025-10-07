vehicle_type = int(input("Please enter vehicle type (1: Motorcycle, 2: Personal Car): "))
if vehicle_type not in [1, 2]:
    hours = float(input("Please enter the number of parking hours: "))
    print("Invalid vehicle type")
else:
    hours = float(input("Please enter the number of parking hours: "))
    if hours <= 0:
        print("Please enter a valid number of parking hours")
    else:
        if hours < 1:
            fee = 0
        else:
            if vehicle_type == 1:
                fee = 10 
                if hours > 1:
                    additional_hours = hours - 1
                    fee += additional_hours * 5
            else:
                fee = 30  
                if hours > 1:
                    additional_hours = hours - 1
                    fee += additional_hours * 15
        print(f"Parking fee: {fee:.2f} THB")