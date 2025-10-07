def parking_calculator():
    """
    Parking Fee Calculator Program
    """
    records = []

    while True:
        is_entry_valid = False
        
        try:
            vt_input = input("Please enter vehicle type (1: Motorcycle, 2: Personal Car): ")
            vehicle_type = int(vt_input)
            
            if vehicle_type not in [1, 2]:
                print("Invalid vehicle type")
            else:
                try:
                    hours_input = input("Please enter the number of parking hours: ")
                    hours = float(hours_input)
                    
                    if hours <= 0:
                        print("Please enter a valid number of parking hours")
                    else:
                        is_entry_valid = True 
                except ValueError:
                    print("Please enter a valid number of parking hours")
        except ValueError:
            print("Invalid vehicle type")
            
        if is_entry_valid:
            cost = 0.0
            if hours < 1:
                cost = 0.0
            elif vehicle_type == 1: 
                cost = 10 + (hours - 1) * 5
            elif vehicle_type == 2: 
                cost = 30 + (hours - 1) * 15
            
            print(f"Parking fee: {cost:.2f} THB")
            records.append((vehicle_type, hours, cost))
            
        continue_choice = input("Do you want to continue? (y/n): ")
        
        
        
        
        if continue_choice.lower() != 'y':
            break

    
    if records:
        print("VT Hours Cost")
        total_cost = 0.0
        for vt, h, c in records:
            print(f"{vt} {h:.2f} {c:.2f}")
            total_cost += c
        print(f"Total {total_cost:.2f} THB")


parking_calculator()