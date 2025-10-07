records = []

while True: 
    try:
        vehicle_type = int(input("Please enter vehicle type (1: Motorcycle, 2: Personal Car):"))
        if  vehicle_type not in [1,2]:
            print("Invalid vehicle type")
            continue
        hours = float(input("Please enter the number of parking hours:"))
        if hours <= 0:
            print("Invalid parking hours. Please enter a number more than 0.")
            continue
    
        if hours < 1:
            fee = 0.00
        else:
            if vehicle_type == 1:
                fee = 10 + (hours - 1) * 5
            elif vehicle_type == 2:
                fee = 30 + (hours - 1) * 15
        
    
        print(f"Parking fee: {fee:.2f} THB")
        records.append((vehicle_type, hours, fee))
    except ValueError:
        print("Invalid input. Please enter numbers only.")
        continue
    cont = input("Do you want to continue? (y/n): ")
    print("------------------------------")
    if cont.lower() !='y':
        break

print("VT Hours Cost")
total = 0
for r in records:
    print(f"{r[0]} {r[1]:.2f} {r[2]:.2f}")
    total += r[2]
print(f"Total {total:.2f} THB")