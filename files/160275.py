parking_list = []

while True:
    print("Please enter vehicle type (1: Motorcycle, 2: Personal Car): ", end="")
    vehicle_type = input().strip()

    
    hours_input = input("Please enter the number of parking hours: ").strip()


    is_valid_hours = (
        hours_input.replace('.', '', 1).isdigit() and 
        hours_input.count('.') <= 1 and 
        (hours_input[0] != '-' or hours_input == "0")
    )

    if not is_valid_hours:
        print("Please enter a valid number of parking hours")
    else:
        hours = float(hours_input)
        if hours <= 0:
            print("Please enter a valid number of parking hours")
        elif vehicle_type != '1' and vehicle_type != '2':
            print("Invalid vehicle type")
        else:
        
            if hours < 1:
                cost = 0.0
            elif vehicle_type == '1':
                cost = 10 + (hours - 1) * 5
            else:  
                cost = 30 + (hours - 1) * 15

            print("Parking fee: {:.2f} THB".format(cost))
            parking_list.append((vehicle_type, hours, cost))

    cont = input("Do you want to continue? (y/n): ").strip().lower()
    print("------------------------------")
    if cont == 'n':
        break

print("VT Hours Cost")
total = 0.0
for vt, hr, fee in parking_list:
    print(f"{vt} {hr:.2f} {fee:.2f}")
    total += fee
print("Total {:.2f} THB".format(total))