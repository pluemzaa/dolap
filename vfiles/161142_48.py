wmotop=0
motoh=0
carh=0
carp=0

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
            print(f"Parking fee: {price:.2f} THB")
            motoh=hour
            motop=price
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
            print(f"Parking fee: {price:.2f} THB")
            carh=hour
            carp=price
    else:
        print("Invalid vehicle type")
    yesno=input("Do you want to continue? (y/n): ")
    print("------------------------------")
    if yesno!='y':
        break

print("VT Hours Cost")
print(f"1 {motoh:.2f} {motop:.2f}")
if carh!=0 and carp!=0:
    print(f"2 {carh:.2f} {carp:.2f}")
    total=motop+carp
    print(f"Total {total:.2f} THB")
else:
    total=motop+carp
    print(f"Total {total:.2f} THB")