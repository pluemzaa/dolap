car = int(input("Please enter vehicle type (1: Motorcycle, 2: Personal Car): "))
time = float(input("Please enter the number of parking hours: "))
price = 0
if car == 1 or car == 2:
    if car == 1:
        if time > 0 and time < 1:
            print(f"Parking fee: {price:.2f} THB")
        elif time == 1 :
            price = 10
            print(f"Parking fee: {price:.2f} THB")
        elif time > 1 :
            price = 5 + (5*time)
            print(f"Parking fee: {price:.2f} THB")
        else:
            print("Please enter a valid number of parking hours")
    if car == 2:
        if time > 0 and time < 1:
            print(f"Parking fee: {price:.2f} THB")
        elif time == 1 :
            price = 30
            print(f"Parking fee: {price:.2f} THB")
        elif time > 1 :
            price = 15 + (15*time)
            print(f"Parking fee: {price:.2f} THB")
        else:
            print("Please enter a valid number of parking hours")
else:
    print("Invalid vehicle type")