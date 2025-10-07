vt = int(input("Please enter vehicle type (1: Motorcycle, 2: Personal Car):"))
ph = float(input("Please enter the number of parking hours:"))
price = 0.00
if vt == 1:
    if ph <= 0:
        print("Please enter a valid number of parking hours")
    elif ph < 1:
        print(f"Parking fee:{price : .2f} THB")
    else:
        price1 = 5
        pc1 = ((ph-1)*price1) + 10
        print(f"Parking fee:{pc1 : .2f} THB")

elif vt == 2:
    if ph <= 0:
        print("Please enter a valid number of parking hours")
    elif ph < 1:
        print(f"Parking fee:{price : .2f}THB")
    else:
        price2 = 15
        pc2 = ((ph-1)*price2) + 30
        print(f"Parking fee:{pc2 : .2f}THB")

else:
    print("Invalid vehicle type")