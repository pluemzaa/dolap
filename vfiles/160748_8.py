transactions = []

while True:
    try:
        vehicle_type = int(input("Please enter vehicle type (1: Motorcycle, 2: Personal Car): "))
        if vehicle_type not in [1, 2]:
            print("Invalid vehicle type")
            continue

        hours = float(input("Please enter the number of parking hours: "))
        if hours <= 0:
            print("Please enter a valid number of parking hours")
            continue

        if hours <= 0.5:
            fee = 0.0
        elif vehicle_type == 1: 
            fee = 10.0 + max(0, hours - 1) * 5
        elif vehicle_type == 2:  
            fee = 30.0 + max(0, hours - 1) * 15

        print(f"Parking fee: {fee:.2f} THB")
        transactions.append((vehicle_type, hours, fee))

    except ValueError:
        print("Invalid input. Please enter a valid number.")
        continue

    continue_input = input("Do you want to continue? (y/n): ").strip().lower()
    if continue_input != 'y':
        break
    print("------------------------------")

print("VT Hours Cost")
total_fee = 0.0
for transaction in transactions:
    vehicle_type, hours, fee = transaction
    print(f"{vehicle_type} {hours:.2f} {fee:.2f}")
    total_fee += fee

print(f"Total {total_fee:.2f} THB")