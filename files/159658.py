vehicle = int(input("Please enter vehicle type (1: Motorcycle, 2: Personal Car): ")) 
time = float(input("Please enter the number of parking hours: "))
fee = 0
if vehicle == 1:
    if time > 0:
        if time < 1:
            fee = 0 * time
            print(f"Parking fee: {fee:.2f} THB")
        elif time == 1:
            fee = 10 * time
            print(f"Parking fee: {fee:.2f} THB")
        else:
            fee = 10+(time-1)*5
            print(f"Parking fee: {fee:.2f} THB")
    else:
        print("Please enter a valid number of parking hours")
elif vehicle == 2:
    if time > 0:
        if time < 1:
            fee = 0 * time
            print(f"Parking fee: {fee:.2f} THB")
        elif time == 1:
            fee = 30 * time
            print(f"Parking fee: {fee:.2f} THB")
        else:
            fee = 30+(time-1)*15
            print(f"Parking fee: {fee:.2f} THB")
    else:
        print("Please enter a valid number of parking hours")
else :
    print("Invalid vehicle type")