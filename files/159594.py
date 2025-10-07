veh = int(input("Please enter vehicle type (1: Motorcycle, 2: Personal Car): "))
st = float(input("Please enter the number of parking hours: "))
price = 0

if veh < 1 or veh > 2:
    print("Invalid vehicle type")
if st < 1:
    print("Please enter a valid number of parking hours")
else:
    if veh == 1:
        if st == 1:
            price = price + 10
            print(f"Parking fee: {price:.2f} THB")
        elif st >1:
            price =( price + 10)+(st*5-5)
            print(f"Parking fee: {price:.2f} THB")
        else:
            print(f"Parking fee: {price:.2f} THB")
    elif veh == 2:
        if st == 1:
            price = price + 30
            print(f"Parking fee: {price:.2f} THB")
        elif st >1:
            price =( price + 30)+(st*15-15)
            print(f"Parking fee: {price:.2f} THB")
        else:
            print(f"Parking fee: {price:.2f} THB")