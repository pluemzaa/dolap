total_fees = []

while True:
    vehicle_type = input("Please enter vehicle type (1: Motorcycle, 2: Personal Car): ")
    if vehicle_type not in ['1', '2']:
        print("Invalid vehicle type")
        break

    hours_input = input("Please enter the number of parking hours: ")
    if not hours_input.replace('.', '', 1).isdigit() or float(hours_input) <= 0:
        print("Please enter a valid number of parking hours")
        break

    hours = float(hours_input)

    if vehicle_type == '1':
        if hours <= 1:
            fee = 0.00
        else:
            fee = 10 + (hours - 1) * 5
    elif vehicle_type == '2':
        if hours <= 1:
            fee = 0.00
        else:
            fee = 30 + (hours - 1) * 15

    print(f"Parking fee: {fee:.2f} THB")
    total_fees.append(fee)

    continue_program = input("Do you want to continue? (yes/no): ").strip().lower()
    if continue_program != 'yes':
        break

if total_fees:
    print("\nSummary of parking fees:")
    for idx, fee in enumerate(total_fees, start=1):
        print(f"Transaction {idx}: {fee:.2f} THB")
    print(f"Total parking fee: {sum(total_fees):.2f} THB")