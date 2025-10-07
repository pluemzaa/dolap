t=float(input("Please enter vehicle type (1: Motorcycle, 2: Personal Car): "))
h=float(input("Please enter the number of parking hours: "))
price=0
if h >0:
    if t==1 or t==2:
            if t==1:
                price = 10+((h-1)*5)
            elif t==2:
                price = 30+((h-1)*15)
            print(f"Parking fee: {price:.2f} THB")

    else:
        print("Invalid vehicle type")    

elif h <= 0:
    print("Parking fee: 0.00 THB")
else:
    print("Please enter a valid number of parking hours")