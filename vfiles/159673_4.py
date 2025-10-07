vehicle=(int(input("Please enter vehicle type (1: Motorcycle, 2: Personal Car):")))
hour=(float(input("Please enter the number of parking hours:")))
if vehicle>2 or vehicle<1:
     print("Invalid vehicle type")
else:
    if vehicle == 1 :
        if hour <= 0 :
            print("Please enter a valid number of parking hours")
        elif hour > 0 and hour < 1 :
            price = hour*0
        elif hour == 1 : 
            price = hour*10
        elif hour > 1 : 
            price = ((hour-1)*5)+10
        else:
            print(f"Parking fee: {price:.2f} THB")
    elif vehicle == 2 :
        if hour <= 0 :
            print("Please enter a valid number of parking hours")
        elif hour > 0 and hour < 1 :
            price = hour*0
        elif hour == 1 : 
            price = hour*30
        elif hour > 1 :
            price = ((hour-1)*15)+30
        else:
            print(f"Parking fee: {price:.2f} THB")