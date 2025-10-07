vehicle_type = input("Please enter vehicle type (1: Motorcycle, 2: Personal Car): ")

if vehicle_type != "1" and vehicle_type != "2":
    print("Invalid vehicle type")
else:
    try:
        hours = float(input("Please enter the number of parking hours: "))

        if hours <= 0:
            print("Please enter a valid number of parking hours")
        elif hours < 1:
            print("Parking fee: 0.00 THB")
        else:
            if vehicle_type == "1":
                first_hour = 10
                additional = (hours - 1) * 5
                fee = first_hour + additional
            else:
                first_hour = 30
                additional = (hours - 1) * 15
                fee = first_hour + additional

            print(f"Parking fee: {fee:.2f} THB")
    except ValueError:
        print("Please enter a valid number of parking hours")