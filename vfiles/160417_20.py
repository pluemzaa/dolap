total_cost = 0.0
records = []

while True:
    try:
        vehicle_type = int(input("Please enter vehicle type (1: Motorcycle, 2: Personal Car): "))
    except:
        print("Invalid vehicle type")
        break

    if vehicle_type not in [1, 2]:
        print("Invalid vehicle type")
        break

    try:
        hours = float(input("Please enter the number of parking hours: "))
    except:
        print("Please enter a valid number of parking hours")
        break

    if hours <= 0:
        print("Please enter a valid number of parking hours")
        break

    # คำนวณค่าจอด
    if hours < 1:
        cost = 0.00
    elif vehicle_type == 1:  # Motorcycle
        cost = 10 + (hours - 1) * 5
    else:  # Personal Car
        cost = 30 + (hours - 1) * 15

    print(f"Parking fee: {cost:.2f} THB")

    records.append((vehicle_type, hours, cost))
    total_cost += cost

    cont = input("Do you want to continue? (y/n): ").strip().lower()
    if cont == 'n':
        break
    print("-" * 30)

# แสดงผลลัพธ์สรุป
if records:
    print("-" * 30)
    print("VT Hours Cost")
    for rec in records:
        vt, h, c = rec
        print(f"{vt} {h:.2f} {c:.2f}")
    print(f"Total {total_cost:.2f} THB")