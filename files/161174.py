parking_records = [] 

while True:
    try:
        vehicle_type = int(input("Please enter vehicle type (1: Motorcycle, 2: Personal Car): "))
        hours = float(input("Please enter the number of parking hours: "))
    except ValueError:
        print("Invalid input. Please enter numbers only.")
        continue

    if vehicle_type not in [1, 2]:
        print("Invalid vehicle type")
    elif hours <= 0:
        print("Please enter a valid number of parking hours")
    else:
        if hours < 1:
            cost = 0.00
        else:
            if vehicle_type == 1:
                cost = 10 + (hours - 1) * 5
            elif vehicle_type == 2:
                cost = 30 + (hours - 1) * 15

        print(f"Parking fee: {cost:.2f} THB")
        parking_records.append((vehicle_type, hours, cost)) 

    cont = input("Do you want to continue? (y/n): ").strip().lower()
    print("-" * 30)
    if cont != 'y':
        break

print("VT Hours Cost")
total = 0
for record in parking_records:
    vt, hr, fee = record
    print(f"{vt} {hr:.2f} {fee:.2f}")
    total += fee

print(f"Total {total:.2f} THB")