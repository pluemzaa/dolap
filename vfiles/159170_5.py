veh = input("Please enter vehicle type (1: Motorcycle, 2: Personal Car): ")
time = float(input("Please enter the number of parking hours:"))

if veh == "1":
    if time < 1 and time > 0:
        print("Parking fee: 0.00 THB")
    elif time <= 0:
        print("Please enter a valid number of parking hours")
    elif time == 1:
        print("Parking fee: 10.00 THB")
    elif time > 1:
        fee = 10+(time - 1) * 5
        print(f"Parking fee: {fee:.2f} THB")
elif veh == "2":
    if time < 1 and time > 0:
        print("Parking fee: 0.00 THB")
    elif time <= 0:
        print("Please enter a valid number of parking hours")
    elif time == 1:
        print("Parking fee: 30.00 THB")
    elif time > 1:
        fee = 30 + (time - 1) * 15
        print(f"Parking fee: {fee:.2f} THB")
else:
    print("Invalid vehicle type")