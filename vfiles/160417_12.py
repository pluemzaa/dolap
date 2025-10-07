vehicles = []
hours_list = []
costs = []

while True:
    print("Please enter vehicle type (1: Motorcycle, 2: Personal Car):", end=" ")
    vt = input().strip()
    if vt not in ["1", "2"]:
        print("Invalid vehicle type")
        cont = input("Do you want to continue? (y/n): ").strip().lower()
        print("------------------------------")
        if cont == 'n':
            break
        else:
            continue

    print("Please enter the number of parking hours:", end=" ")
    try:
        hrs = float(input().strip())
        if hrs <= 0:
            print("Please enter a valid number of parking hours")
            cont = input("Do you want to continue? (y/n): ").strip().lower()
            print("------------------------------")
            if cont == 'n':
                break
            else:
                continue
    except:
        print("Please enter a valid number of parking hours")
        cont = input("Do you want to continue? (y/n): ").strip().lower()
        print("------------------------------")
        if cont == 'n':
            break
        else:
            continue

    # คำนวณค่าจอด
    if hrs < 1:
        fee = 0.00
    elif vt == "1":
        fee = 10 + (hrs - 1) * 5
    else:  # vt == "2"
        fee = 30 + (hrs - 1) * 15

    print(f"Parking fee: {fee:.2f} THB")
    vehicles.append(vt)
    hours_list.append(hrs)
    costs.append(fee)

    cont = input("Do you want to continue? (y/n): ").strip().lower()
    print("------------------------------")
    if cont == 'n':
        break

# แสดงผลรวม
if len(costs) > 0:
    print("VT Hours Cost")
    total = 0
    for i in range(len(costs)):
        print(f"{vehicles[i]} {hours_list[i]:.2f} {costs[i]:.2f}")
        total += costs[i]
    print(f"Total {total:.2f} THB")