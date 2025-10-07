v = int(input("Please enter vehicle type (1: Motorcycle, 2: Personal Car): "))
h = float(input("Please enter the number of parking hours: "))

fee = 0
if not v in [1, 2]:
    print("Invalid vehicle type")
elif h < 0:
    print("Please enter a valid number of parking hours")
elif h >= 1:
    if v == 1:
        fee = 10
        if h >= 2:
            fee += 5*(h-1)
    else:
        fee = 30
        if h >= 2:
            fee += 15*(h-1)
    print("Parking fee: %.2f THB" %fee)
else:
    print("Parking fee: 0.00 THB")