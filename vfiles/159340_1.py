t=input("Please enter vehicle type (1: Motorcycle, 2: Personal Car): ")
h=float(input("Please enter the number of parking hours: "))
if t=="1":
    if h <1:
        h=10
        print(f"Parking fee: {h:.2f} THB")
    else:
        h*5
        print(f"Parking fee: {h:.2f} THB")