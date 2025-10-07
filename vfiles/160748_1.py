valid_records = []

while True:
    
    vehicle_type = input("Please enter vehicle type (1: Motorcycle, 2: Personal Car): ")

    
    if vehicle_type not in ['1', '2']:
        print("Invalid vehicle type")
        break

    
    parking_hours = float(input("Please enter the number of parking hours: "))

   
    if parking_hours <= 0:
        print("Please enter a valid number of parking hours")
        break

   
    if parking_hours <= 1:
        parking_fee = 0.00
    elif vehicle_type == '1':
        parking_fee = 10 + (parking_hours - 1) * 5
    elif vehicle_type == '2':
        parking_fee = 30 + (parking_hours - 1) * 15

    
    print(f"Parking fee: {parking_fee:.2f} THB")

    
    valid_records.append((vehicle_type, parking_hours, parking_fee))

    
    continue_input = input("Do you want to continue? (y/n): ")
    if continue_input.lower() != 'y':
        break

    print("-------------------------------")
print("VT Hours Cost")
total_cost = 0.00
for record in valid_records:
    vehicle_type, parking_hours, parking_fee = record
    print(f"{vehicle_type} {parking_hours:.2f} {parking_fee:.2f}")
    total_cost += parking_fee

print(f"Total {total_cost:.2f} THB")