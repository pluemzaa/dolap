v = int(input("Please enter vehicle type (1: Motorcycle, 2: Personal Car):"))
h = float(input("Please enter the number of parking hours:"))
fee = 0
if v==1 :
    if h <= 0 :
        print("Please enter a valid number of parking hours")
    elif h > 0 and h < 1 :
        fee = 0 
    elif h == 1 :
        fee = 10 
    else  :
        fee = 10 + (h-1)*5
    print(f"Parking fee: {fee:.2f}THB")
elif v==2 :
    if h <= 0 :
        print("Please enter a valid number of parking hours")
    elif h > 0 and h < 1 :
        fee = 0 
    elif h == 1 :
        fee = 30 
    else :
        fee = 30 + (h-1)*15
    print(f"Parking fee: {fee:.2f}THB")
else:
    print("Invalid vehicle type")