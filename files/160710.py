parking_records = []

while True:
    print("Please enter vehicle type (1: Motorcycle, 2: Personal Car): ", end='')
    try:
        vehicle_type = int(input())
    except ValueError:
        print("Invalid vehicle type")
        break

    print("Please enter the number of parking hours: ", end='')
    try:
        hours = float(input())
    except ValueError:
        print("Please enter a valid number of parking hours")
        break

    if vehicle_type not in [1, 2]:
        print("Invalid vehicle type")
    elif hours <= 0:
        print("Please enter a valid number of parking hours")
    else:
        if hours < 1:
            fee = 0.00
        else:
            if vehicle_type == 1:  # Motorcycle
                fee = 10 + (hours - 1) * 5
            elif vehicle_type == 2:  # Personal Car
                fee = 30 + (hours - 1) * 15

        print(f"Parking fee: {fee:.2f} THB")
        parking_records.append((vehicle_type, hours, fee))

    print("Do you want to continue? (y/n): ", end='')
    cont = input().strip().lower()
    print("-" * 30)
    if cont != 'y':
        break

# แสดงผลสรุป
print("VT Hours Cost")
total = 0
for record in parking_records:
    vt, hrs, cost = record
    print(f"{vt} {hrs:.2f} {cost:.2f}")
    total += cost
print(f"Total {total:.2f} THB")