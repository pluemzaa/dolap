v = int(input("Please enter vehicle type (1: Motorcycle, 2: Personal Car): "))
h = float(input("Please enter the number of parking hours: "))
cost =  0
if v ==1:
    if h < 0:
        print("Please enter a valid number of parking hours")
    elif h < 1:
        cost = 0
        print(f"Parking fee: {cost:2f} THB")
    else:
        cost = 5
        cost = ((h-1)*cost) + 10
        print(f"Parking fee: {cost:.2f} THB")
elif v == 2:
    if h < 0:
        print("Please enter a valid number of parking hours")
    elif h < 1:
        cost = 0
        print(f"Parking fee: {cost:.2f} THB")
    else:
        cost = 15
        cost = ((h-1)*cost) + 30
        print(f"Parking fee: {cost:.2f} THB")
else:
    print("Invalid vehicle type")