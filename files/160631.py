vehicle_type = input("Enter vehicle type (1: Motorcycle, 2: Personal Car): ")
try:
    vehicle_type = int(vehicle_type)
except ValueError:
    print("Invalid vehicle type")
    exit()

if vehicle_type != 1 and vehicle_type != 2:
    print("Invalid vehicle type")
    exit()

try:
    hours = float(input("Enter number of parking hours: "))
except ValueError:
    print("Please enter a valid number of parking hours")
    exit()

if hours <= 0:
    print("Please enter a valid number of parking hours")
    exit()
elif hours < 1:
    print("Parking fee: 0.00 THB")
else:
    
    first_hour = 1
    extra_hours = hours - first_hour

    if vehicle_type == 1:  # Motorcycle
        fee = 10 + (extra_hours * 5)
    elif vehicle_type == 2:  # Personal Car
        fee = 30 + (extra_hours * 15)

    print(f"Parking fee: {fee:.2f} THB")