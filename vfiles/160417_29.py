vehicle_data = []

while True:
    print("Please enter vehicle type (1: Motorcycle, 2: Personal Car):", end=" ")
    try:
        vehicle_type = int(input())
    except:
        print("Invalid vehicle type")
        break

    if vehicle_type not in [1, 2]:
        print("Invalid vehicle type")
        break

    print("Please enter the number of parking hours:", end=" ")
    try:
        hours = float(input())
    except:
        print("Please enter a valid number of parking hours")
        break

    if hours < 0:
        print("Please enter a valid number of parking hours")
        break

    if hours < 1:
        cost = 0.00
    else:
        if vehicle_type == 1:
            cost = 10 + (hours - 1) * 5
        else:
            cost = 30 + (hours - 1) * 15

    print(f"Parking fee: {cost:.2f} THB")
    vehicle_data.append((vehicle_type, hours, cost))

    print("Do you want to continue? (y/n):", end=" ")
    cont = input().strip().lower()
    if cont != 'y':
        break
    print("------------------------------")

print("VT Hours Cost")
total = 0.0
for v, h, c in vehicle_data:
    print(f"{v} {h:.2f} {c:.2f}")
    total += c
print(f"Total {total:.2f} THB")