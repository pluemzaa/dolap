def calculate_parking_fee():
    is_input_valid = True
    
    vehicle_type_str = input("Please enter vehicle type (1: Motorcycle, 2: Personal Car): ")
    
    vehicle_type = 0
    if not vehicle_type_str.isdigit():
        print("Invalid vehicle type")
        is_input_valid = False
    else:
        vehicle_type = int(vehicle_type_str)
        if vehicle_type != 1 and vehicle_type != 2:
            print("Invalid vehicle type")
            is_input_valid = False

    parking_hours = 0.0
    if is_input_valid:
        parking_hours_str = input("Please enter the number of parking hours: ")

        decimal_point_count = 0
        is_numeric_float = True
        
        if parking_hours_str == "" or parking_hours_str == ".":
            is_numeric_float = False
        else:
            for char in parking_hours_str:
                if char == '.':
                    decimal_point_count += 1
                elif not char.isdigit():
                    is_numeric_float = False
                    break
            
        if not is_numeric_float or decimal_point_count > 1:
            print("Please enter a valid number of parking hours")
            is_input_valid = False
        else:
            parking_hours = float(parking_hours_str)
            if parking_hours <= 0:
                print("Please enter a valid number of parking hours")
                is_input_valid = False

    if is_input_valid:
        parking_fee = 0.0
        
        if parking_hours < 1:
            parking_fee = 0.0
        elif vehicle_type == 1:
            parking_fee = 10.0
            if parking_hours > 1:
                parking_fee += (parking_hours - 1) * 5.0
        elif vehicle_type == 2:
            parking_fee = 30.0
            if parking_hours > 1:
                parking_fee += (parking_hours - 1) * 15.0
        
        print(f"Parking fee: {parking_fee:.2f} THB")

calculate_parking_fee()