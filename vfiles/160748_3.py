parking_records = []

while True:
    try:
        vehicle_type = int(input("Please enter vehicle type (1: Motorcycle, 2: Personal Car): "))
        if vehicle_type not in [1, 2]:
            print("Invalid vehicle type")
            break

        hours = float(input("Please enter the number of parking hours: "))
        if hours <= 0:
            print("Please enter a valid number of parking hours")
            break

        if vehicle_type == 1:
            if hours <= 1:
                fee = 0
            elif hours <= 2:
                fee = 10
            else:
                fee = 10 + (hours - 1) * 5
        elif vehicle_type == 2:
            if hours <= 1:
                fee = 0
            elif hours <= 2:
                fee = 30
            else:
                fee = 30 + (hours - 1) * 15

        print(f"Parking fee: {fee:.2f} THB")
        parking_records.append((vehicle_type, hours, fee))

        cont = input("Do you want to continue? (y/n): ").strip().lower()
        if cont != 'y':
            break

    except ValueError:
        print("Please enter a valid number of parking hours")
        break

print("VT Hours Cost")
total_cost = 0
for record in parking_records:
    vehicle_type, hours, cost = record
    print(f"{vehicle_type} {hours:.2f} {cost:.2f}")
    total_cost += cost

print(f"Total {total_cost:.2f} THB")