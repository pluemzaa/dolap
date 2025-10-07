vehicle_type = input("Please enter vehicle type (1: Motorcycle, 2: Personal Car): ")
if vehicle_type not in ['1', '2']:
    print("Invalid vehicle type")
    exit()

try:
    hours = float(input("Please enter the number of parking hours: "))
except:
    print("Please enter a valid number of parking hours")
    exit()

if hours <= 0:
    print("Please enter a valid number of parking hours")
    exit()

if hours < 1:
    print("Parking fee: 0.00 THB")
    exit()

if vehicle_type == '1':
    fee = 10 + (hours - 1) * 5
elif vehicle_type == '2':
    fee = 30 + (hours - 1) * 15

print(f"Parking fee: {fee:.2f} THB")