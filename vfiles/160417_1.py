vehicles = []
hours_list = []
costs = []

while True:
    print("Please enter vehicle type (1: Motorcycle, 2: Personal Car):", end=" ")
    vt = input()

    if vt not in ["1", "2"]:
        print("Invalid vehicle type")
    else:
        print("Please enter the number of parking hours:", end=" ")
        try:
            hours = float(input())
            if hours <= 0:
                print("Please enter a valid number of parking hours")
            else:
                # คำนวณค่าจอด
                if vt == "1":  # มอไซค์
                    if hours <= 1:
                        cost = 10.00
                    else:
                        cost = 10 + (hours - 1) * 5
                else:  # รถยนต์
                    if hours <= 1:
                        cost = 30.00
                    else:
                        cost = 30 + (hours - 1) * 15

                print(f"Parking fee: {cost:.2f} THB")
                vehicles.append(int(vt))
                hours_list.append(hours)
                costs.append(cost)
        except:
            print("Please enter a valid number of parking hours")

    print("Do you want to continue? (y/n):", end=" ")
    cont = input().lower()
    print("-" * 25, "( copy ไปเลย )")
    if cont == "n":
        break

# สรุปผล
print("VT Hours Cost")
total = 0
for i in range(len(vehicles)):
    print(f"{vehicles[i]} {hours_list[i]:.2f} {costs[i]:.2f}")
    total += costs[i]
print(f"Total {total:.2f} THB")