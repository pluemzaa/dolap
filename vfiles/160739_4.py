records = []

while True:
    print("Please enter vehicle type (1: Motorcycle, 2: Personal Car): ", end="")
    try:
        vehicle_type = int(input())
    except:
        print("Invalid vehicle type")
        break

    if vehicle_type not in [1, 2]:
        print("Invalid vehicle type")
        break

    print("Please enter the number of parking hours: ", end="")
    try:
        hours = float(input())
    except:
        print("Please enter a valid number of parking hours")
        break

    if hours <= 0:
        print("Please enter a valid number of parking hours")
    else:
        if hours < 1:
            fee = 0.00
        else:
            first_hour = 1
            remaining_hours = hours - 1
            if vehicle_type == 1:
                # Motorcycle: 10 THB first hour, 5 THB each next hour
                fee = 10 + remaining_hours * 5
            elif vehicle_type == 2:
                # Personal Car: 30 THB first hour, 15 THB each next hour
                fee = 30 + remaining_hours * 15
        print(f"Parking fee: {fee:.2f} THB")

        # Save only valid records
        records.append((vehicle_type, hours, fee))

    print("Do you want to continue? (y/n): ", end="")
    cont = input().strip().lower()
    print("-" * 30)
    if cont != 'y':
        break

# Print summary
if records:
    print("VT Hours Cost")
    total = 0
    for r in records:
        print(f"{r[0]} {r[1]:.2f} {r[2]:.2f}")
        total += r[2]
    print(f"Total {total:.2f} THB")