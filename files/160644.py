parking_data = [] 
total_fee = 0.0

while True:
    try:
        vehicle_type = int(input("Please enter vehicle type (1: Motorcycle, 2: Personal Car): "))
        hours = float(input("Please enter the number of parking hours: "))

        if vehicle_type not in [1, 2]:
            print("Invalid vehicle type")
        elif hours <= 0:
            print("Please enter a valid number of parking hours")
        else:
            if hours < 1:
                fee = 0.0
            else:
                if vehicle_type == 1:
                    fee = 10 + (hours - 1) * 5
                elif vehicle_type == 2:
                    fee = 30 + (hours - 1) * 15

            print(f"Parking fee: {fee:.2f} THB")
            parking_data.append((vehicle_type, hours, fee))
            total_fee += fee

    except ValueError:
        print("Invalid input. Please enter numbers only.")

    cont = input("Do you want to continue? (y/n): ").strip().lower()
    print("------------------------------")
    if cont != 'y':
        break

print("VT Hours Cost")
for vt, hrs, cost in parking_data:
    print(f"{vt} {hrs:.2f} {cost:.2f}")
print(f"Total {total_fee:.2f} THB")