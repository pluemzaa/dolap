a = float(input("Please enter vehicle type (1: Motorcycle, 2: Personal Car):"))
b = float(input("Please enter the number of parking hours:"))


if a == 1:
    if b >= 1:
        if b >= 1 and b < 2:
            print("Parking fee: 10.00 THB")
        else:
            print("Parking fee: %.2f" %(+(b-1)*5 +10),"THB")
    elif b < 0:
            print("Please enter a valid number of parking hours")
    else:
        print("Parking fee: 0.00 THB")
elif a == 2:
    if b >= 1:
        if b >= 1 and b < 2:
            print("Parking fee: 30.00 THB")
        else:
            print("Parking fee: %.2f" %(+(b-1)*15 +30),"THB")
    elif b < 0:
            print("Please enter a valid number of parking hours")
    else:
        print("Parking fee: 0.00 THB")
else:
    print("Invalid vehicle type")