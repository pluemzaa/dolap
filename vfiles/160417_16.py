def calculate_fee(vehicle_type, hours):
    if vehicle_type == 1:
        if hours <= 1:
            return hours * 10
        else:
            return 10 + (hours - 1) * 5
    elif vehicle_type == 2:
        if hours <= 1:
            return hours * 30
        else:
            return 30 + (hours - 1) * 15

all_data = []
total_cost = 0

while True:
    try:
        vt = int(input("Please enter vehicle type (1: Motorcycle, 2: Personal Car): "))
        if vt not in [1, 2]:
            print("Invalid vehicle type")
            continue

        hours = float(input("Please enter the number of parking hours: "))
        if hours <= 0:
            print("Please enter a valid number of parking hours")
            continue

        fee = calculate_fee(vt, hours)
        print(f"Parking fee: {fee:.2f} THB")
        all_data.append((vt, hours, fee))
        total_cost += fee

        cont = input("Do you want to continue? (y/n): ").strip().lower()
        if cont == 'n':
            break
    except:
        print("Please enter a valid number of parking hours")

print("----------------------------")
print("VT Hours Cost")
for data in all_data:
    print(f"{data[0]} {data[1]} {data[2]:.2f}")
print(f"Total {total_cost:.2f} THB")