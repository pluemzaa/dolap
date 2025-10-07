def calculate_fee(vehicle_type, hours):
    if vehicle_type == 1:
        return 10 + (hours - 1) * 5 if hours > 1 else hours * 10
    elif vehicle_type == 2:
        return 30 + (hours - 1) * 15 if hours > 1 else hours * 30

all_data = []
total_cost = 0

while True:
    try:
        vt = int(input("Please enter vehicle type (1: Motorcycle, 2: Personal Car):"))
        if vt not in [1, 2]:
            print("Invalid vehicle type")
            continue
    except:
        print("Invalid vehicle type")
        continue

    try:
        hours = float(input("Please enter the number of parking hours:"))
        if hours <= 0:
            print("Please enter a valid number of parking hours")
            continue
    except:
        print("Please enter a valid number of parking hours")
        continue

    fee = calculate_fee(vt, hours)
    print(f"Parking fee: {fee:.2f} THB")
    total_cost += fee
    all_data.append((vt, hours, fee))

    cont = input("Do you want to continue? (y/n):")
    if cont.lower() == 'n':
        break

print("--------------------------------")
print("VT Hours Cost")
for i in all_data:
    print(f"{i[0]} {i[1]} {i[2]:.2f}")
print(f"Total {total_cost:.2f} THB")