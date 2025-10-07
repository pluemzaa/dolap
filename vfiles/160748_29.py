def calculate_parking_fee(vehicle_type, hours):
    if hours <= 0:
        print("Please enter a valid number of parking hours")
        return None
    if hours < 1:
        return 0.00
    if vehicle_type == 1:  
        if hours <= 1:
            return 10.00
        else:
            return 10.00 + (hours - 1) * 5.00
    elif vehicle_type == 2:  
        if hours <= 1:
            return 30.00
        else:
            return 30.00 + (hours - 1) * 15.00
    else:
        print("Invalid vehicle type")
        return None

def main():
    records = []
    while True:
        try:
            vehicle_type = int(input("Please enter vehicle type (1: Motorcycle, 2: Personal Car): "))
            hours = float(input("Please enter the number of parking hours: "))
            
            fee = calculate_parking_fee(vehicle_type, hours)
            if fee is not None:
                print(f"Parking fee: {fee:.2f} THB")
                records.append((vehicle_type, hours, fee))
            else:
                
                return
            
            cont = input("Do you want to continue? (y/n): ").lower()
            if cont != 'y':
                break
            print("------------------------------")
        except ValueError:
            print("Please enter a valid number of parking hours")
            continue
    
    
    if records:
        print("------------------------------")
        print("VT Hours Cost")
        total = 0.0
        for vt, h, cost in records:
            print(f"{vt} {h:.2f} {cost:.2f}")
            total += cost
        print(f"Total {total:.2f} THB")

if __name__ == "__main__":
    main()