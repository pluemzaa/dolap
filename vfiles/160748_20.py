total_fees = 0.0
valid_entries = 0

while True:
    
    vehicle_type = input("Please enter vehicle type (1: Motorcycle, 2: Personal Car): ")
    
    
    if vehicle_type.lower() == 'exit':
        break
    
    
    try:
        vehicle_type = int(vehicle_type)
    except ValueError:
        print("Invalid vehicle type")
        break
    
    if vehicle_type not in [1, 2]:
        print("Invalid vehicle type")
        break
    
    hours_input = input("Please enter the number of parking hours: ")
    
   
    try:
        hours = float(hours_input)
    except ValueError:
        print("Please enter a valid number of parking hours")
        break
    
    if hours <= 0:
        print("Please enter a valid number of parking hours")
        break
    
    
    fee = 0.0
    
    if hours <= 1:
        fee = 0.0
    else:
        if vehicle_type == 1: 
            fee = 10 + (hours - 1) * 5
        elif vehicle_type == 2: 
            fee = 30 + (hours - 1) * 15
    
    
    total_fees += fee
    valid_entries += 1
    
    
    print(f"Parking fee: {fee:.2f} THB")


if valid_entries > 0:
    print(f"\nTotal parking fees for {valid_entries} valid entries: {total_fees:.2f} THB")
else:
    print("\nNo valid parking entries were processed.")