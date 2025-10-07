t=input("Please enter vehicle type (1: Motorcycle, 2: Personal Car): ")
h=float(input("Please enter the number of parking hours: "))

if t=="1":
    if h<= 0:
        print("Please enter a valid number of parking hours")
    elif h<1:
        print("Parking fee: 0.00 THB")
    elif h>=1:
        m = 10 + ((h-1)*5)
        print(f"Parking fee: {m:.2f} THB")

elif t=="2":   
    if h<= 0:
        print("Please enter a valid number of parking hours")
    elif h<1:
        print("Parking fee: 0.00 THB")
    elif h>=1:
        c = 30 + ((h-1)*15)
        print(f"Parking fee: {c:.2f} THB")
else :
    print("Invalid vehicle type")