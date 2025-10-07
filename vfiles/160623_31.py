parking_records = []

while True:
    vehicle_type_input = input("Please enter vehicle type (1: Motorcycle, 2: Personal Car): ")
    if vehicle_type_input == "1" or vehicle_type_input == "2":
        vehicle_type = int(vehicle_type_input)
    else:
        print("Invalid vehicle type")
        cont = input("Do you want to continue? (y/n): ")
        print("------------------------------")
        if cont != 'y':
            break
        continue

    hours_input = input("Please enter the number of parking hours: ")

    is_valid = True
    dot_found = False
    for ch in hours_input:
        if ch == '.':
            if dot_found:
                is_valid = False
                break
            dot_found = True
        elif not ch:
            is_valid = False
            break

    if not is_valid or hours_input == "":
        print("Please enter a valid number of parking hours")
        cont = input("Do you want to continue? (y/n): ")
        print("------------------------------")
        if cont != 'y':
            break
        continue

    hours = float(hours_input)

    if hours <= 0:
        print("Please enter a valid number of parking hours")
        cont = input("Do you want to continue? (y/n): ")
        print("------------------------------")
        if cont != 'y':
            break
        continue

    if hours < 1:
        fee = 0.00
    else:
        if int(hours) != hours:
            total_hours = int(hours) + 1
        else:
            total_hours = int(hours)

        if vehicle_type == 1:
            fee = 10 + (total_hours - 1) * 5
        else:
            fee = 30 + (total_hours - 1) * 15

    print("Parking fee: %.2f THB" % fee)

    parking_records.append([vehicle_type, hours, fee])

    cont = input("Do you want to continue? (y/n): ")
    print("------------------------------")
    if cont != 'y':
        break

print("VT Hours Cost")
total = 0.0
for record in parking_records:
    print("%d %.2f %.2f" % (record[0], record[1], record[2]))
    total = total + record[2]
print("Total %.2f THB" % total)