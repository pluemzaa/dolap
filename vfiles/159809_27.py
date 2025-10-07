vehicle_type = input("Please enter vehicle type (1: Motorcycle, 2: Personal Car): ")

if vehicle_type != "1" and vehicle_type != "2":
    print("Invalid vehicle type")
    exit()

parking_hours = input("Please enter the number of parking hours: ")

try:
    hours = float(parking_hours)
    if hours <= 0:
        print("Please enter a valid number of parking hours")
    elif hours < 1:
        print("Parking fee: 0.00 THB")
    else:
        if vehicle_type == "1":
            fee = 10 + (hours - 1) * 5
        else:
            fee = 30 + (hours - 1) * 15
        print("Parking fee: {:.2f} THB".format(fee))
except:
    print("Please enter a valid number of parking hours")