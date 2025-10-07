vtype = input("Please enter vehicle type (1: Motorcycle, 2: Personal Car): ")
hours = input("Please enter the number of parking hours: ")

try:
    h = float(hours)

    if vtype != "1" and vtype != "2":
        print("Invalid vehicle type")

    elif h <= 0:
        print("Please enter a valid number of parking hours")

    elif h < 1:
        print("Parking fee: 0.00 THB")

    elif vtype == "1":
        fee = 10 + (h - 1) * 5
        print("Parking fee: %.2f THB" % fee)

    elif vtype == "2":
        fee = 30 + (h - 1) * 15
        print("Parking fee: %.2f THB" % fee)

    else:
        print("Something went wrong")

except:
    print("Please enter a valid number of parking hours")