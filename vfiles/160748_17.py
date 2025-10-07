total_fees = 0.0
continue_program = True

while continue_program:
    vehicle_input = input("Please enter vehicle type (1: Motorcycle, 2: Personal Car): ")

    
    if not vehicle_input.isdigit():
        print("Invalid vehicle type")
        break

    vehicle_type = int(vehicle_input)
    if vehicle_type != 1 and vehicle_type != 2:
        print("Invalid vehicle type")
        break

    hours_input = input("Please enter the number of parking hours: ")

    
    if hours_input.count('.') > 1 or hours_input.replace('.', '', 1).isdigit() == False:
        print("Please enter a valid number of parking hours")
        break

    hours = float(hours_input)
    if hours <= 0:
        print("Please enter a valid number of parking hours")
        break

    
    if hours < 1:
        fee = 0.0
    else:
        if vehicle_type == 1:
            fee = 10 + (hours - 1) * 5
        else:
            fee = 30 + (hours - 1) * 15

    print(f"Parking fee: {fee:.2f} THB")
    total_fees += fee

    cont = input("Do you want to continue? (y/n): ").strip().lower()
    if cont != 'y':
        continue_program = False

print(f"\nTotal parking fee (valid entries only): {total_fees:.2f} THB")