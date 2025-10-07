vehicles = []
hours_list = []
costs = []

while True:
    print("Please enter vehicle type (1: Motorcycle, 2: Personal Car):", end=" ")
    vehicle = input()
    
    print("Please enter the number of parking hours:", end=" ")
    try:
        hour = float(input())
    except:
        hour = -1  # ทำให้ระบบเตะออก

    if vehicle not in ["1", "2"]:
        print("Invalid vehicle type")
    elif hour <= 0:
        print("Please enter a valid number of parking hours")
    else:
        if hour < 1:
            fee = 0.00
        elif vehicle == "1":
            fee = 10 + (hour - 1) * 5
        elif vehicle == "2":
            fee = 30 + (hour - 1) * 15

        print(f"Parking fee: {fee:.2f} THB")
        vehicles.append(int(vehicle))
        hours_list.append(hour)
        costs.append(fee)

    print("Do you want to continue? (y/n):", end=" ")
    cont = input().lower()
    print("------------------------------ ( copy ไปเลย)")
    if cont == "n":
        break

if costs:
    print("VT Hours Cost")
    total = 0
    for i in range(len(costs)):
        print(f"{vehicles[i]} {hours_list[i]:.2f} {costs[i]:.2f}")
        total += costs[i]
    print(f"Total {total:.2f} THB")