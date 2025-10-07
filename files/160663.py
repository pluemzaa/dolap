parking_data = []

while True:
    try:
        vehicle_type = int(input("Please enter vehicle type (1: Motorcycle, 2: Personal Car): "))
        hours = float(input("Please enter the number of parking hours: "))

        
        if vehicle_type not in [1, 2]:
            print("Invalid vehicle type")
            valid = False
        
        elif hours <= 0:
            print("Please enter a valid number of parking hours")
            valid = False
        else:
            
            if hours < 1:
                cost = 0.00
            elif vehicle_type == 1:
                cost = 10 + (hours - 1) * 5
            elif vehicle_type == 2:
                cost = 30 + (hours - 1) * 15

            print(f"Parking fee: {cost:.2f} THB")
            parking_data.append([vehicle_type, hours, cost])
            valid = True

    except ValueError:
        print("Invalid input. Please enter numbers only.")
        valid = False

    cont = input("Do you want to continue? (y/n): ").lower()
    print("------------------------------")
    if cont != 'y':
        break

print("VT Hours Cost")
total = 0
for vt, hrs, fee in parking_data:
    print(f"{vt} {hrs:.2f} {fee:.2f}")
    total += fee
print(f"Total {total:.2f} THB")