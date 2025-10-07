def calculate_parking_fee(vehicle_type, hours):
    if vehicle_type == 1:
        if hours <= 1:
            return 0.0
        else:
            return 10 + (hours - 1) * 5
    elif vehicle_type == 2:
        if hours <= 1:
            return 0.0
        else:
            return 30 + (hours - 1) * 15
    else:
        return None

def main():
    parking_records = []

    while True:
        try:
            vehicle_type = int(input("Please enter vehicle type (1: Motorcycle, 2: Personal Car): "))
            if vehicle_type not in [1, 2]:
                print("Invalid vehicle type")
                continue

            hours = float(input("Please enter the number of parking hours: "))
            if hours <= 0:
                print("Please enter a valid number of parking hours")
                continue

            fee = calculate_parking_fee(vehicle_type, hours)
            if fee is not None:
                parking_records.append((vehicle_type, hours, fee))
                print(f"Parking fee: {fee:.2f} THB")

            continue_input = input("Do you want to continue? (y/n): ").strip().lower()
            if continue_input != 'y':
                break

        except ValueError:
            print("Please enter a valid number of parking hours")

    print("------------------------------")
    print("VT Hours Cost")
    total_fee = 0
    for record in parking_records:
        vehicle_type, hours, fee = record
        print(f"{vehicle_type} {hours:.2f} {fee:.2f}")
        total_fee += fee
    print(f"Total {total_fee:.2f} THB")

if __name__ == "__main__":
    main()