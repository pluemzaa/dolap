vehicles = []
hours_list = []
costs = []

while True:
    try:
        vehicle_type = int(input("Please enter vehicle type (1: Motorcycle, 2: Personal Car): "))
        if vehicle_type not in [1, 2]:
            print("Invalid vehicle type")
            continue
    except ValueError:
        print("Invalid vehicle type")
        continue

    try:
        hours = float(input("Please enter the number of parking hours: "))
        if hours < 0:
            raise ValueError
    except ValueError:
        print("Please enter a valid number of parking hours")
        continue

    if hours < 1:
        fee = 0.0
    elif vehicle_type == 1:
        fee = hours * 10
    else:
        fee = hours * 30

    print(f"Parking fee: {fee:.2f} THB")

    vehicles.append(vehicle_type)
    hours_list.append(hours)
    costs.append(fee)

    cont = input("Do you want to continue? (y/n): ").lower()
    if cont == "n":
        break

if costs:
    print("\nVT Hours Cost")
    total = 0
    for i in range(len(costs)):
        print(f"{vehicles[i]} {hours_list[i]:.2f} {costs[i]:.2f}")
        total += costs[i]
    print(f"Total {total:.2f} THB")