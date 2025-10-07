parking_records = []

while True:
    try:
        vehicle_type = int(input("Please enter vehicle type (1: Motorcycle, 2: Personal Car): "))
        hours = float(input("Please enter the number of parking hours: "))
        
        if vehicle_type not in [1, 2]:
            print("Invalid vehicle type")
        elif hours <= 0:
            print("Please enter a valid number of parking hours")
        else:
            
            if hours < 1:
                fee = 0.0
            else:
                if vehicle_type == 1: 
                    fee = 10 + (hours - 1) * 5
                elif vehicle_type == 2: 
                    fee = 30 + (hours - 1) * 15
            
            print(f"Parking fee: {fee:.2f} THB")
            parking_records.append((vehicle_type, hours, fee))
    except ValueError:
        print("Invalid input")
        continue

    cont = input("Do you want to continue? (y/n): ").strip().lower()
    if cont != 'y':
        break
    print("------------------------------")

print("------------------------------")
print("VT Hours Cost")
total = 0.0
for record in parking_records:
    vt, hr, cost = record
    print(f"{vt} {hr:.2f} {cost:.2f}")
    total += cost
print(f"Total {total:.2f} THB")