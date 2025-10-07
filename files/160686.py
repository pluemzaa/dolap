parking_data = []
total_cost = 0

while True:
    print("Please enter vehicle type (1: Motorcycle, 2: Personal Car):", end=' ')
    vehicle_input = input()

    if vehicle_input != '1' and vehicle_input != '2':
        print("Invalid vehicle type")
        continue

    vehicle_type = int(vehicle_input)

    print("Please enter the number of parking hours:", end=' ')
    hour_input = input()


    if hour_input.replace('.', '', 1).isdigit() == False:
        print("Please enter a valid number of parking hours")
        continue

    hours = float(hour_input)

    if hours <= 0:
        print("Please enter a valid number of parking hours")
    else:
        if hours < 1:
            fee = 0.00
        else:
            if vehicle_type == 1:
                fee = 10 + (hours - 1) * 5
            else:
                fee = 30 + (hours - 1) * 15

        print(f"Parking fee: {fee:.2f} THB")
        parking_data.append([vehicle_type, hours, fee])
        total_cost += fee

    cont = input("Do you want to continue? (y/n): ").lower()
    print("------------------------------")
    if cont != 'y':
        break


print("VT Hours Cost")
for data in parking_data:
    print(f"{data[0]} {data[1]:.2f} {data[2]:.2f}")
print(f"Total {total_cost:.2f} THB")