def calculate_parking_fee(vehicle_type, hours):
    if hours < 1:
        return 0.00
    if vehicle_type == 1:
        return 10 + (hours - 1) * 5
    elif vehicle_type == 2:
        return 30 + (hours - 1) * 15

def main():
    records = []
    total = 0.00

    while True:
        try:
            vehicle_type = int(input("Please enter vehicle type (1: Motorcycle, 2: Personal Car): "))
        except:
            print("Invalid vehicle type")
            break

        if vehicle_type not in [1, 2]:
            print("Invalid vehicle type")
            break

        try:
            hours = float(input("Please enter the number of parking hours: "))
        except:
            print("Please enter a valid number of parking hours")
            cont = input("Do you want to continue? (y/n): ").lower()
            if cont != 'y':
                print("------------------------------")
                break
            print("------------------------------")
            continue