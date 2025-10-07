records = []
total_cost = 0

while True:
    try:
        
        vehicle_type = int(input("Please enter vehicle type (1: Motorcycle, 2: Personal Car): "))

        if vehicle_type not in [1, 2]:
            print("Invalid vehicle type")
            break
        
        hours = float(input("Please enter the number of parking hours: "))
        
        if hours <= 0:
            print("Please enter a valid number of parking hours")
            continue
        if hours < 1:
            fee = 0.00
        else:
            if vehicle_type == 1:  
                fee = 10 + (hours - 1) * 5
            else:  
                fee = 30 + (hours - 1) * 15
        
        print(f"Parking fee: {fee:.2f} THB")
        
        records.append({
            'vehicle_type': vehicle_type,
            'hours': hours,
            'fee': fee
        })
        total_cost += fee
        
        
        continue_choice = input("Do you want to continue? (y/n): ").lower()
        if continue_choice != 'y':
            break
            
    except ValueError:
        print("Please enter valid input")
        continue

if records:
    print("\nVT Hours Cost")
    for record in records:
        print(f"{record['vehicle_type']} {record['hours']:.2f} {record['fee']:.2f}")
    print(f"Total {total_cost:.2f} THB")