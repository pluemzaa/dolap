x = int(input("Please enter vehicle type (1: Motorcycle, 2: Personal Car): "))
y = float(input("Please enter the number of parking hours: "))
Thb = 0

if y < 0:
  print("Please enter a valid number of parking hours")
elif x==1:
    if y<1 :
        print ("Parking fee: 0.00 THB" )
    elif y >=1 and y<2:
        Thb =  y * 10 
    elif y >=2 :
        Thb = 10+((y-1)*5)
    print (f"Parking fee: {Thb:.2f} THB" )  
elif x==2:
    if y<1 :
       print ("Parking fee: 0.00 THB" )
    elif y >=1 and y<2:
       Thb =  y * 30
    elif y >=2 :
       Thb = 30+((y-1)*30)
    print (f"Parking fee: {Thb:.2f} THB" )  
else :
  print("Invalid vehicle type")