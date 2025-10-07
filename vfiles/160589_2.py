c = 0 
b = 0
cc = 0
cb = 0
cx = 0
cy = 0

while True:
    menu = int(input("Please enter vehicle type (1: Motorcycle, 2: Personal Car): "))
    time = float(input("Please enter the number of parking hours: "))

    if menu == 1:
        cc = cc + 1
        if time <= 0 :
            print("Please enter a valid number of parking hours")
            
        elif 0 < time < 1: 
            c = 0
            print(f"Parking fee: {c:.2f} THB")
            cx = cx+c
        elif 1 <= time < 2:
            c = 10
            print(f"Parking fee: {c:.2f} THB")
            cx = cx+c
        elif time > 2 :
            c = 5 +(time*5)
            print(f"Parking fee: {c:.2f} THB")
            cx = cx+c

        
    elif menu == 2:
        cb = cb + 1
        if time <= 0:
            print("Please enter a valid number of parking hours")
        elif 0 < time < 1:
            b = 0
            print(f"Parking fee: {b:.2f} THB")
            cy = cy+b
        elif 1 <= time < 2:
            b = 15
            print(f"Parking fee: {b:.2f} THB")
            cy = cy+b
        elif time > 2:
            b = 15 +(time*15)
            print(f"Parking fee: {b:.2f} THB")
            cy = cy+b
        else:
            print("Invalid vehicle type")
    
    x = input("Continute (y/n) : ")
    if x =="n":
        break