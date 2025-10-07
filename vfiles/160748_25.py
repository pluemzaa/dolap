total_fee = 0.0
valid_records = 0

while True:
    
    vehicle_input = input("Please enter vehicle type (1: Motorcycle, 2: Personal Car): ")
    

    if not vehicle_input.isdigit():
        print("Invalid vehicle type")
        break
    
    vehicle_type = int(vehicle_input)
    

    if vehicle_type != 1 and vehicle_type != 2:
        print("Invalid vehicle type")
        break
    
    
    hours_input = input("Please enter the number of parking hours: ")
    

    is_valid_number = True
    if hours_input.count('.') > 1:
        is_valid_number = False
    else:
        for char in hours_input:
            if not (char.isdigit() or char == '.' or char == '-'):
                is_valid_number = False
                break
    
    if not is_valid_number or hours_input == '' or hours_input == '.':
        print("Please enter a valid number of parking hours")
        break
    
    hours = float(hours_input)
    
    
    if hours <= 0:
        print("Please enter a valid number of parking hours")
        break
    
    
    fee = 0.0
    
    
    if hours < 1:
        fee = 0.0
    else:
        if vehicle_type == 1:  
            if hours <= 1:
                fee = 10.0
            else:
                fee = 10.0 + (hours - 1) * 5.0
        else:
            if hours <= 1:
                fee = 30.0
            else:
                fee = 30.0 + (hours - 1) * 15.0
    
    print(f"Parking fee: {fee:.2f} THB")
    
    
    total_fee += fee
    valid_records += 1
    
    
    continue_choice = input("Do you want to continue? (y/n): ").lower()
    if continue_choice != 'y':
        break