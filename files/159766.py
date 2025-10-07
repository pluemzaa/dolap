vehicle_type = int(input("Please enter vehicle type (1: Motorcycle, 2: Personal Car): "))
hours = float(input("Please enter the number of parking hours: "))

if hours <= 0:
    print("Please enter a valid number of parking hours")
elif vehicle_type == 1:
    fee = 0.0 if hours < 1 else 10 + (hours - 1) * 5
    print(f"Parking fee: {fee:.2f} THB")
elif vehicle_type == 2:
    fee = 0.0 if hours < 1 else 30 + (hours - 1) * 15
    print(f"Parking fee: {fee:.2f} THB")
else:
    print("Invalid vehicle type")