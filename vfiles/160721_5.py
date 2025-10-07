parking_list = []
total = 0

while True:
    vehicle_type = input("Please enter vehicle type (1: Motorcycle, 2: Personal Car): ")
    if vehicle_type not in ['1', '2']:
        print("Invalid vehicle type")
        continue

    hours_input = input("Please enter the number of parking hours: ")
    try:
        hours = float(hours_input)
        if hours < 0:
            print("Please enter a valid number of parking hours")
            cont = input("Do you want to continue? (y/n): ")
            if cont.lower() != 'y':
                break
            else:
                continue  
    except ValueError:
        print("Please enter a valid number of parking hours")
        cont = input("Do you want to continue? (y/n): ")
        if cont.lower() != 'y':
            break
        else:
            continue  

    
    if hours < 1:
        fee = 0.00
    elif vehicle_type == '1':
        fee = 10 + (hours - 1) * 5
    else:  
        fee = 30 + (hours - 1) * 15

    print(f"Parking fee: {fee:.2f} THB")
    parking_list.append((vehicle_type, hours, fee))
    total += fee

    cont = input("Do you want to continue? (y/n): ")
    if cont.lower() != 'y':
        break


print("\nVT Hours Cost")
for vt, hrs, cost in parking_list:
    print(f"{vt} {hrs:.2f} {cost:.2f}")
print(f"Total {total:.2f} THB")