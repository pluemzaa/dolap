vehicle = input("Please enter vehicle type (1: Motorcycle, 2: Personal Car): ")
hours = float(input("Please enter the number of parking hours: "))

if vehicle != "1" and vehicle != "2":
    print("Invalid vehicle type")

if hours <= 0.00:
    print("Please enter a valid number of parking hours")

if vehicle == "1" and hours == 1.00:
    print("Parking fee: 10.00 THB")
elif vehicle == "1" and hours > 1.00:
    fee_v = (hours * 5) + 10
    print("Parking fee: %.2f THB"%fee_v)
elif vehicle == "2" and hours == 1.00:
    print("Parking fee: 30.00 THB")
elif vehicle == "2" and hours > 1.00:
    fee_p = (hours * 15) + 30
    print("Parking fee: %.2f THB"%fee_p)