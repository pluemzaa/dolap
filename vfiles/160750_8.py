records = []

while True:
    try:
        # Get vehicle type
        vehicle_type = int(input("Please enter vehicle type (1: Motorcycle, 2: Personal Car): "))
        if vehicle_type not in [1, 2]:
            print("Invalid vehicle type")
            continue

        # Get parking hours
        hours = float(input("Please enter the number of parking hours: "))
        if hours <= 0:
            print("Please enter a valid number of parking hours")
            continue

        # Calculate parking fee
        if vehicle_type == 1:
            if hours <= 1:
                fee = 10.0
            else:
                fee = 10.0 + (hours - 1) * 5.0
        elif vehicle_type == 2:
            if hours <= 1:
                fee = 30.0
            else:
                fee = 30.0 + (hours - 1) * 15.0

        print(f"Parking fee: {fee:.2f} THB")

        # Save record
        records.append((vehicle_type, hours, fee))

        # Ask if user wants to continue
        cont = input("Do you want to continue? (y/n): ").strip().lower()
        if cont != 'y':
            break

    except ValueError:
        print("Invalid input. Please try again.")

# Display final summary
print("\nVT Hours Cost")
total = 0.0
for r in records:
    vt, hrs, cost = r
    print(f"{vt} {hrs:.2f} {cost:.2f}")
    total += cost
print(f"Total: {total:.2f} THB")