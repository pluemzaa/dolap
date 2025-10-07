records = []
total_cost = 0.0

while True:
    vehicle_input = input("Please enter vehicle type (1: Motorcycle, 2: Personal Car): ")
    hours_input = input("Please enter the number of parking hours: ")

    if not vehicle_input.isdigit() or not hours_input.replace('.', '', 1).isdigit():
        print("Invalid input")
        cont = input("Do you want to continue? (y/n): ").lower()
        print("------------------------------")
        if cont != 'y':
            break
        continue

    vehicle_type = int(vehicle_input)
    hours = float(hours_input)

    if vehicle_type not in [1, 2]:
        print("Invalid vehicle type")
        cont = input("Do you want to continue? (y/n): ").lower()
        print("------------------------------")
        if cont != 'y':
            break
        continue

    if hours <= 0:
        print("Please enter a valid number of parking hours")
        cont = input("Do you want to continue? (y/n): ").lower()
        print("------------------------------")
        if cont != 'y':
            break
        continue

    if hours < 1:
        cost = 0.0
    else:
        if vehicle_type == 1:  
            cost = 10 + (hours - 1) * 5
        elif vehicle_type == 2:  
            cost = 30 + (hours - 1) * 15

    print(f"Parking fee: {cost:.2f} THB")

    records.append((vehicle_type, hours, cost))
    total_cost += cost

    cont = input("Do you want to continue? (y/n): ").lower()
    print("------------------------------")
    if cont != 'y':
        break

print("VT Hours Cost")
for vt, h, c in records:
    print(f"{vt} {h:.2f} {c:.2f}")
print(f"Total {total_cost:.2f} THB")