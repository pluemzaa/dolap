type = float(input("Please enter vehicle type (1: Motorcycle, 2: Personal Car): "))
time = float(input("Please enter a valid number of parking hours: "))
price = 0
if time <= 0:
    print("Please enter a valid number of parking hours")
elif type > 2:
    print("Invalid vehicle type")
elif type==1:
    if time == 1:
        price = time*10
    elif time >=2:
        price = time*6.43
    else:
        price = time*0
    print(f"Parking fee: {price:.2f} THB")
elif type==2:
    if time == 1:
        price = time*30
    elif time >=2:
        price = time*16.43
    else:
        price = time*0
    print(f"Parking fee: {price:.2f} THB")