Vehicle = int(input("Please enter vehicle type (1: Motorcycle, 2: Personal Car): "))
Hours = float(input("Please enter the number of parking hours: "))

if Vehicle not in [1, 2]:
    print("Invalid vehicle type")
elif Hours < 0:
    print("Please enter a valid number of parking hours")
elif Hours < 1:
    print("Parking fee: 0.00 THB")
elif Vehicle == 1:
    PriceMotorcycle = 10 + (Hours - 1) * 5
    print("Parking fee: %.2f THB" % PriceMotorcycle)
elif Vehicle == 2:
    PriceMotorPersonalcar = 30 + (Hours - 1) * 15
    print("Parking fee: %.2f THB" % PriceMotorPersonalcar)