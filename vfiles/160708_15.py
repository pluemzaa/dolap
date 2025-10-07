#while True:
motor1 = int(input("Please enter vehicle type (1: Motorcycle, 2: Personal Car): "))
fee1 = float(input("Please enter the number of parking hours: "))

if motor1 == 1:
    motor1 = 1
    if fee1 < 1 and fee1 > 0:
        abcd1 = fee1*0
        print(f"Parking fee: {abcd1:.2f} THB")
    elif fee1 < 0:
        print("Please enter a valid number of parking hours")
        abcd1 = 0
    else:
        abcd1 = 10+((fee1-1)*5)
        print(f"Parking fee: {abcd1:.2f} THB")
elif motor1 == 2:
    motor1 = 2
    if fee1 < 1:
        abcd1 = fee1*0
        print(f"Parking fee: {abcd1:.2f} THB")
    elif fee1 < 0:
        print("Please enter a valid number of parking hours")
        abcd1 = 0
    else:
        abcd1 = 30+((fee1-1)*15)
        print(f"Parking fee: {abcd1:.2f} THB")
else:
    print("Invalid vehicle type")
    abcd1 = 0

fee2 = 0
motor2 = 0
abcd2 = 0
while True:    
    z = input("Do you want to continue? (y/n): ")
    print("------------------------------")

    if z == "y":
        motor2 = int(input("Please enter vehicle type (1: Motorcycle, 2: Personal Car): "))
        fee2 = float(input("Please enter the number of parking hours: "))
        if motor2 == 1:
            motor2 = 1
            if fee2 < 1:
                abcd2 = fee2*0
                print(f"Parking fee: {abcd2:.2f} THB")
            elif fee2 < 0:
                print("Please enter a valid number of parking hours")
                abcd2 = 0
            else:
                abcd2 = 10+((fee2-1)*5)
                print(f"Parking fee: {abcd2:.2f} THB")
        elif motor2 == 2:
            motor2 = 2 
            if fee2 < 1:
                abcd2 = fee2*0
                print(f"Parking fee: {abcd2:.2f} THB")
            elif fee2 < 0:
                print("Please enter a valid number of parking hours")
                abcd2 = 0
            else:
                abcd2 = 30+((fee2-1)*15)
                print(f"Parking fee: {abcd2:.2f} THB")
        else:
            print("Invalid vehicle type")
            abcd2 = 0
        
    elif z == "n":
        pass
        break
    else:
        pass
    

    
print("VT Hours Cost",end="\n")
if fee1 > 0:
    if motor1 == 1:
            
        print(f"{motor1} {fee1:.2f} {abcd1:.2f}")   
    elif motor1 == 2:
            
        print(f"{motor1} {fee1:.2f} {abcd1:.2f}")
if fee2 > 0:
        
    if motor2 == 1:
            
        print(f"{motor2} {fee2:.2f} {abcd2:.2f}")   
    elif motor2 == 2:
            
        print(f"{motor2} {fee2:.2f} {abcd2:.2f}")
print(f"Total {abcd1 + abcd2:.2f} THB")