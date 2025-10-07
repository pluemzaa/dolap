records = []

while True:
    print("Please enter vehicle type (1: Motorcycle, 2: Personal Car): ", end="")
    try:
        vehicle_type = int(input())
    except:
        print("Invalid vehicle type")
        print("Do you want to continue? (y/n): ", end="")
        cont = input().strip().lower()
        print("-" * 30)
        if cont != 'y':
            break
        continue

    if vehicle_type not in [1, 2]:
        print("Invalid vehicle type")
        print("Do you want to continue? (y/n): ", end="")
        cont = input().strip().lower()
        print("-" * 30)
        if cont != 'y':
            break
        continue

    print("Please enter the number of parking hours: ", end="")
    try:
        hours = float(input())
    except:
        print("Please enter a valid number of parking hours")
        print("Do you want to continue? (y/n): ", end="")
        cont = input().strip().lower()
        print("-" * 30)
        if cont != 'y':
            break
        continue

    if hours <= 0:
        print("Please enter a valid number of parking hours")
        print("Do you want to continue? (y/n): ", end="")
        cont = input().strip().lower()
        print("-" * 30)
        if cont != 'y':
            break
        continue

    # คำนวณค่าจอด
    if hours < 1:
        fee = 0.00
    else:
        if vehicle_type == 1:
            fee = 10 + (hours - 1) * 5
        else:
            fee = 30 + (hours - 1) * 15

    print(f"Parking fee: {fee:.2f} THB")
    records.append((vehicle_type, hours, fee))

    print("Do you want to continue? (y/n): ", end="")
    cont = input().strip().lower()
    print("-" * 30)
    if cont != 'y':
        break

# สรุปผล
if records:
    print("VT Hours Cost")
    total = 0
    for r in records:
        print(f"{r[0]} {r[1]:.2f} {r[2]:.2f}")
        total += r[2]
    print(f"Total {total:.2f} THB")