def calculate_parking_fee():
    total_fees = 0.0
    valid_entries = 0
    
    while True:
        try:
        
            vehicle_type = input("Please enter vehicle type (1: Motorcycle, 2: Personal Car): ")
            
            
            if vehicle_type.lower() == 'exit':
                break
                
            
            vehicle_type = int(vehicle_type)
            
            
            if vehicle_type not in [1, 2]:
                print("Invalid vehicle type")
                break
                
            
            hours = float(input("Please enter the number of parking hours: "))
            
           
            if hours <= 0:
                print("Please enter a valid number of parking hours")
                break
                
            
            fee = 0.0
            
            if hours <= 1:
                fee = 0.0
            else:
                if vehicle_type == 1:  # 摩托车
                    fee = 10 + (hours - 1) * 5
                elif vehicle_type == 2:  # 私家车
                    fee = 30 + (hours - 1) * 15
            
        
            total_fees += fee
            valid_entries += 1
        
            
            print(f"Parking fee: {fee:.2f} THB")
            
        except ValueError:
            print("Invalid input. Please enter numbers only.")
            break
    
    
    if valid_entries > 0:
        print(f"\nTotal parking fees for {valid_entries} valid entries: {total_fees:.2f} THB")
    else:
        print("\nNo valid parking entries were processed.")


calculate_parking_fee()