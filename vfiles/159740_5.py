vehicle_type = input("Please enter vehicle type (1: Motorcycle, 2: Personal Car): ")

if vehicle_type not in ["1", "2"]:
    print("Invalid vehicle type")
else:
    try:
        vehicle_type = int(vehicle_type)
 
        hours = float(input("Please enter the number of parking hours: "))

        if hours <= 0:
            print("Please enter a valid number of parking hours")
        else:
            if hours < 1:
                fee = 0.00
            else:
                first_hour = 1
                extra_hours = hours - first_hour

                if vehicle_type == 1:  
                    fee = 10 + (extra_hours * 5)
                elif vehicle_type == 2:
                    fee = 30 + (extra_hours * 15)

            print(f"Parking fee: {fee:.2f} THB")
    except ValueError:
        print("Please enter a valid number of parking hours")