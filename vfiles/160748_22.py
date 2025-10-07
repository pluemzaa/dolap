total_fees = []

while True:
    try:
        vehicle_type = int(input("Please enter vehicle type (1: Motorcycle, 2: Personal Car): "))
        hours = float(input("Please enter the number of parking hours: "))

        if hours <= 0:
            print("Please enter a valid number of parking hours")
            break

        if vehicle_type == 1:
            if hours <= 1:
                fee = 0.00
            else:
                fee = 10 + (hours - 1) * 5
        elif vehicle_type == 2:
            if hours <= 1:
                fee = 0.00
            else:
                fee = 30 + (hours - 1) * 15
        else:
            print("Invalid vehicle type")
            break

        print(f"Parking fee: {fee:.2f} THB")
        total_fees.append(fee)

        continue_program = input("Do you want to continue? (yes/no): ").strip().lower()
        if continue_program != 'yes':
            break
    except ValueError:
        print("Invalid input. Please enter valid numbers.")
        break

if total_fees:
    print("Summary of parking fees:")
    for idx, fee in enumerate(total_fees, start=1):
        print(f"Transaction {idx}: {fee:.2f} THB")
    print(f"Total parking fee: {sum(total_fees):.2f} THB")