MTT = 0
MTF = 0
CTT = 0
CTF = 0

while True:
    fee = 0
    vehi = int(input("Please enter vehicle type (1: Motorcycle, 2: Personal Car): "))
    
    if vehi == 1:
        time = float(input("Please enter the number of parking hours: "))
        if time >= 0:
            if time < 1:
                fee = 0
            elif time == 1:
                fee = 10
            else:
                fee = 10 + (time - 1) * 5
            print(f"Parking fee: {fee:05.2f} THB")
            MTT += time
            MTF += fee
        else:
            print("Please enter a valid number of parking hours")
    
    elif vehi == 2:
        time = float(input("Please enter the number of parking hours: "))
        if time >= 0:
            if time < 1:
                fee = 0
            elif time == 1:
                fee = 30
            else:
                fee = 30 + (time - 1) * 15
            print(f"Parking fee: {fee:05.2f} THB")
            CTT += time
            CTF += fee
        else:
            print("Please enter a valid number of parking hours")
    
    else:
        print("Invalid vehicle type")
    
    cont = input("Do you want to continue? (y/n): ").lower()
    print("------------------------------")
    
    if cont == 'n':
        print("VT Hours Cost")
        print(f"1 {MTT:.2f} {MTF:05.2f}")
        print(f"2 {CTT:.2f} {CTF:05.2f}")
        print(f"Total {(MTF + CTF):.2f} THB")
        break