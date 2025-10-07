summary = []

while True:
    vehicle_type_input = input("Please enter vehicle type (1: Motorcycle, 2: Personal Car): ")
    hours_input = input("Please enter the number of parking hours: ")

    valid = True 

    if not hours_input.replace('.', '', 1).isdigit():
        print("Please enter a valid number of parking hours")
        valid = False
    else:
        hours = float(hours_input)
        if hours <= 0:
            print("Please enter a valid number of parking hours")
            valid = False

    if not vehicle_type_input.isdigit():
        print("Invalid vehicle type")
        valid = False
    else:
        vehicle_type = int(vehicle_type_input)
        if vehicle_type != 1 and vehicle_type != 2:
            print("Invalid vehicle type")
            valid = False

    if valid:
        if hours < 1:
            fee = 0.00
        elif vehicle_type == 1:
            fee = 10 + (hours - 1) * 5
        elif vehicle_type == 2:
            fee = 30 + (hours - 1) * 15

        print(f"Parking fee: {fee:.2f} THB")
        summary.append((vehicle_type, hours, fee))

    cont = input("Do you want to continue? (y/n): ").strip().lower()
    print("------------------------------")
    if cont != 'y':
        break

if summary:
    print("VT Hours Cost")
    total = 0
    for vtype, h, f in summary:
        print(f"{vtype} {h:.2f} {f:.2f}")
        total += f
    print(f"Total {total:.2f} THB")