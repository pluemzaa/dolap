vehicle_type = input("Please enter vehicle type (1: Motorcycle, 2: Personal Car): ")
hours_input = input("Please enter the number of parking hours: ")

if hours_input.count('.') > 1 or not hours_input.replace('.', '', 1).isdigit():
    print("Please enter a valid number of parking hours")
    exit()

hours = float(hours_input)

if hours <= 0:
    print("Please enter a valid number of parking hours")
    exit()

if vehicle_type != "1" and vehicle_type != "2":
    print("Invalid vehicle type")
    exit()

if hours < 1:
    fee = 0.00
elif vehicle_type == "1":
    fee = 10 + (hours - 1) * 5
else:  # vehicle_type == "2"
    fee = 30 + (hours - 1) * 15

print(f"Parking fee: {fee:.2f} THB")