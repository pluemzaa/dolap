vehicle = int(input("Please enter vehicle type (1: Motorcycle, 2: Personal Car):"))
hours = float(input("Please enter the number of parking hours: "))

if vehicle not in [1, 2]:
    print("Invalid vehicle type")
elif hours < 0:
    print("Please enter a valid number of parking hours")
elif hours < 1:
    print("Parking fee: 0.00 THB")
elif vehicle == 1:
    PriceMotorcycle = 10 + (hours - 1) * 15
    print("Parking fee: %.2f THB" % PriceMotorcycle)
elif vehicle == 2:
    PriceMotorPersonalcar = 30 + (hours - 1) * 15
    print("Parking fee: %.2f THB" % PriceMotorPersonalcar)