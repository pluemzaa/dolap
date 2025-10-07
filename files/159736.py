v = int(input("Please enter vehicle type (1: Motorcycle, 2: Personal Car):"))
h = float(input("Please enter the number of parking hours:"))

if v not in [1, 2]:
    print("Invalid vehicle type")
elif h < 0:
    print("Please enter a valid number of parking hours")
elif h < 1:
    print("Parking fee: 00.00 THB")
elif v == 1:
    printc = 10 + (h - 1) * 5
    print("Parking fee: %.2f THB" % printc)
elif v == 2:
    printp = 30 + (h - 1) * 15
    print("Parking fee: %.2f THB" % printp)