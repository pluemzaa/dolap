summary = []

while True:
    vehicle_type_input = input("Please enter vehicle type (1: Motorcycle, 2: Personal Car): ")
    if not vehicle_type_input.isdigit():
        print("Invalid vehicle type")
        continue
    vehicle_type = int(vehicle_type_input)

    if vehicle_type != 1 and vehicle_type != 2:
        print("Invalid vehicle type")
        continue

    try:
        hours = float(input("Please enter the number of parking hours: "))
    except ValueError:
        print("Please enter a valid number of parking hours")
        continue

    if hours < 0:
        print("Please enter a valid number of parking hours")
        continue

    if hours == 0.00:
        fee = 0.00
    elif vehicle_type == 1:
        fee = 10 + (hours - 1) * 5
    elif vehicle_type == 2:
        fee = 30 + (hours - 1) * 15

    print(f"Parking Fee: {fee:.2f} THB")

    summary.append((vehicle_type, hours, fee))

    cont = input("Do you want to continue? (y/n): ").strip().lower()
    if cont != 'y':
        break

print("\n--- Hours Cost ---")
total_fee = 0
for vtype, h, f in summary:
    print(f"Vehicle Type: {vtype} | Hours: {h:.2f} | Fee: {f:.2f} THB")
    total_fee += f
    
print(f"Total: {total_fee:.2f} THB")