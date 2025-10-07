V = int(input("Please enter vehicle type (1: Motorcycle, 2: Personal Car):"))
H = float(input("Please enter the number of parking hours:"))
if V==1:
    if H < 0:
        print("Please enter a valid number of parking hours")
    elif H >=0 and H < 1:
        cost = 0
        print(f"Parking fee: {cost:.2f} THB")
    else:
        cost = (H-1)*5+10
        print(f"Parking fee: {cost:.2f} THB")
elif V==2:
    if H < 0:
        print("Please enter a valid number of parking hours")
    elif H >=0 and H < 1:
        cost = 0
        print(f"Parking fee: {cost:.2f} THB")
    else:
        cost = (H-1)*15+30
        print(f"Parking fee: {cost:.2f} THB")
else:
    print("Invalid vehicle type")