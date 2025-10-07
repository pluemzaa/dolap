vehicles = []
hours_list = []
costs = []

while True:
    print("Please enter vehicle type (1: Motorcycle, 2: Personal Car): ", end="")
    vt = input().strip()
    
    if vt not in ["1", "2"]:
        print("Invalid vehicle type")
        break

    print("Please enter the number of parking hours: ", end="")
    try:
        hrs = float(input().strip())
    except:
        print("Please enter a valid number of parking hours")
        break

    if hrs <= 0:
        print("Please enter a valid number of parking hours")
        break

    # คำนวณค่าจอด
    if hrs < 1:
        fee = 0.00
    elif vt == "1":
        fee = 10 + (hrs - 1) * 5
    elif vt == "2":
        fee = 30 + (hrs - 1) * 15

    print(f"Parking fee: {fee:.2f} THB")

    vehicles.append(vt)
    hours_list.append(hrs)
    costs.append(fee)

    print("Do you want to continue? (y/n): ", end="")
    cont = input().strip().lower()
    print("------------------------------")
    if cont == "n":
        break

# สรุปผล
if len(costs) > 0:
    print("VT Hours Cost")
    total = 0
    for i in range(len(costs)):
        print(f"{vehicles[i]} {hours_list[i]:.2f} {costs[i]:.2f}")
        total += costs[i]
    print(f"Total {total:.2f} THB")