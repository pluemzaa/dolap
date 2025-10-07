while True:
    vehicle=(int(input("Please enter vehicle type (1: Motorcycle, 2: Personal Car): ")))
    hour=(float(input("Please enter the number of parking hours: ")))
    price=0
    if vehicle==1 :
        if hour>0 and hour <1 :
            price= 0
        if hour>=1 and hour<2 : 
            price= 10
        if hour>2 : 
            price= ((hour-1)*5)+10
        if hour<=0 :
            print("Please enter a valid number of parking hours")
        else:
            hour
            price
            print(f"Parking fee: {price:.2f} THB")
    elif vehicle==2 :
        if hour>0 and hour <1 :
            price=0
        if hour>=1 and hour<2 : 
            price=30
        if hour>2 :
            price= ((hour-1)*15)+30
        if hour<=0 :
            print("Please enter a valid number of parking hours")
        else:
            hour
            price
            print(f"Parking fee: {price:.2f} THB")
    else:
        print("Invalid vehicle type")
    yesno=input("Do you want to continue? (y/n): ")
    print("------------------------------ ( copy ไปเลย)")
    if yesno!='y':
        break

print("VT Hours Cost")
print(f"1: {hour:.2f} {price:.2f}")
print(f"2: {hour:.2f} {price:.2f}")
total=price+price
print(f"Total: {total:.2f} THB")