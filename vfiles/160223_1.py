parking_list = []  # เก็บรายการจอดที่ถูกต้อง

while True:
    print("Please enter vehicle type (1: Motorcycle, 2: Personal Car): ", end="")
    vehicle_type = input().strip()

    if vehicle_type not in ['1', '2']:
        print("Invalid vehicle type")
    else:
        try:
            hours = float(input("Please enter the number of parking hours: "))
            if hours <= 0:
                print("Please enter a valid number of parking hours")
            else:
                cost = 0.0
                if hours < 1:
                    cost = 0.0
                else:
                    if vehicle_type == '1':  # Motorcycle
                        cost = 10 + (hours - 1) * 5
                    elif vehicle_type == '2':  # Personal Car
                        cost = 30 + (hours - 1) * 15
                print("Parking fee: {:.2f} THB".format(cost))
                parking_list.append((vehicle_type, hours, cost))
        except:
            print("Please enter a valid number of parking hours")

    # ถามว่าจะทำต่อไหม
    cont = input("Do you want to continue? (y/n): ").strip().lower()
    print("------------------------------")
    if cont != 'y':
        break

# สรุปรายการ
print("VT Hours Cost")
total = 0.0
for item in parking_list:
    vt, hr, fee = item
    print(f"{vt} {hr:.2f} {fee:.2f}")
    total += fee
print("Total {:.2f} THB".format(total))