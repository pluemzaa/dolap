parking_list = []

while True:
    print("Please enter vehicle type (1: Motorcycle, 2: Personal Car): ", end="")
    vehicle_type = input().strip()

    if vehicle_type != '1' and vehicle_type != '2':
        print("Invalid vehicle type")
    else:
        hours_input = input("Please enter the number of parking hours: ").strip()

        # ตรวจสอบว่าเป็นตัวเลขทศนิยมหรือจำนวนเต็มเท่านั้น (รองรับ 0.5, 3.75, ฯลฯ)
        if (hours_input.replace('.', '', 1).isdigit() and hours_input.count('.') <= 1 and hours_input[0] != '-'):
            hours = float(hours_input)
            if hours <= 0:
                print("Please enter a valid number of parking hours")
            else:
                # คำนวณค่าจอดรถ
                if hours < 1:
                    cost = 0.0
                elif vehicle_type == '1':
                    cost = 10 + (hours - 1) * 5
                else:  # vehicle_type == '2'
                    cost = 30 + (hours - 1) * 15

                print("Parking fee: {:.2f} THB".format(cost))
                parking_list.append((vehicle_type, hours, cost))
        else:
            print("Please enter a valid number of parking hours")

    cont = input("Do you want to continue? (y/n): ").strip().lower()
    print("------------------------------")
    if cont != 'y':
        break

# สรุปผล
print("VT Hours Cost")
total = 0.0
for vt, hr, fee in parking_list:
    print(f"{vt} {hr:.2f} {fee:.2f}")
    total += fee
print("Total {:.2f} THB".format(total))