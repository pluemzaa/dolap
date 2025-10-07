car = int(input("Please enter vehicle type (1: Motorcycle, 2: Personal Car): "))
h = float(input("Please enter the number of parking hours: "))
if car == 1 :
    if h == 1 :
     print(f'Parking fee:{(h*10): .2f} THB')
    elif h > 1 :
        h=h-1
        print(f'Parking fee:{(h*5)+10: .2f} THB')
    elif h <= 0 :
        print("Please enter a valid number of parking hours ")
    elif h < 1 : 
        print("Parking fee: 0.00 THB")
elif car == 2 :
    if h == 1 :
        print(f'Parking fee:{(h*30): .2f} THB')
    elif h > 1 :
        h=h-1
        print(f'Parking fee:{(h*15)+30: .2f} THB')
    elif h < 0 :
        print("Please enter a valid number of parking hours ")
    elif h < 1 :
        print("Parking fee: 0.00 THB")
else :
    print("Invalid vehicle type")