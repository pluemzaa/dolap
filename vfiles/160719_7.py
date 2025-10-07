parking_records = ""
total_cost = 0
record_count = 0

while True:
    vehicle_type = int(input("Please enter vehicle type (1: Motorcycle, 2: Personal Car): "))
    
    if vehicle_type not in [1, 2]:
        hours = float(input("Please enter the number of parking hours: "))
        print("Invalid vehicle type")
        break
    
    hours = float(input("Please enter the number of parking hours: "))
    
    if hours <= 0:
        print("Please enter a valid number of parking hours")
        cont = input("Do you want to continue? (y/n): ")
        if cont == 'n':
            break
        else:
            print("------------------------------")
            continue
    
    if hours < 1:
        fee = 0.0
    elif vehicle_type == 1:
        if hours <= 1:
            fee = 10.0
        else:
            fee = 10.0 + (hours - 1) * 5.0
    elif vehicle_type == 2:
        if hours <= 1:
            fee = 30.0
        else:
            fee = 30.0 + (hours - 1) * 15.0
    
    print(f"Parking fee: {fee:.2f} THB")
    
    parking_records = parking_records + f"{vehicle_type} {hours:.2f} {fee:.2f}\n"
    total_cost += fee
    record_count += 1
    
    cont = input("Do you want to continue? (y/n): ")
    if cont == 'n':
        break
    else:
        print("------------------------------")

if record_count > 0:
    print("------------------------------")
    print("VT Hours Cost")
    print(parking_records, end="")
    print(f"Total {total_cost:.2f} THB")