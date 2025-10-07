def calculate_parking_fee(vehicle_type, hours):
    if vehicle_type == 1:
        if hours <= 0.5:
            return 0.0
        elif hours <= 1:
            return 10.0
        else:
            return 10.0 + (hours - 1) * 5
    elif vehicle_type == 2:
        if hours <= 0.5:
            return 0.0
        elif hours <= 1:
            return 30.0
        else:
            return 30.0 + (hours - 1) * 15
    else:
        return None

def main():
    total_fee = 0.0
    while True:
        try:
            vehicle_type = int(input("Please enter vehicle type (1: Motorcycle, 2: Personal Car): "))
            if vehicle_type not in [1, 2]:
                print("Invalid vehicle type")
                break

            hours = float(input("Please enter the number of parking hours: "))
            if hours <= 0:
                print("Please enter a valid number of parking hours")
                break

            fee = calculate_parking_fee(vehicle_type, hours)
            if fee is not None:
                print(f"Parking fee: {fee:.2f} THB")
                total_fee += fee

            another = input("Do you want to calculate another parking fee? (yes/no): ").strip().lower()
            if another != 'yes':
                break

        except ValueError:
            print("Invalid input. Please enter a valid number.")
            break

    print(f"Total parking fee: {total_fee:.2f} THB")

if __name__ == "__main__":
    main()