MTT = 0  
MTF = 0  
CTT = 0  
CTF = 0 

while True:
    fee = 0
    vehi = int(input("Please enter vehicle type (1: Motorcycle, 2: Personal Car): "))
    
    if vehi == 1:
        time = float(input("Please enter the number of parking hours: "))
        if time > 0:
            if time == 1:
                fee = 10
                print(f"Parking fee: {fee:.2f} THB")
            elif time < 1:
                fee = 0
                print(f"Parking fee: 0.00 THB")
            else:
                fee = 10 + (time - 1) * 5
                print(f"Parking fee: {fee:.2f} THB")
            MTT += time
            MTF += fee
        else:
            print("Please enter a valid number of parking hours")

    elif vehi == 2:
        time = float(input("Please enter the number of parking hours: "))
        if time > 0:
            if time == 1:
                fee = 30
                print(f"Parking fee: {fee:.2f} THB")
            elif time < 1:
                fee = 0
                print(f"Parking fee: 0.00 THB")
            else:
                fee = 30 + (time - 1) * 15
                print(f"Parking fee: {fee:.2f} THB")
            CTT += time
            CTF += fee
        else:
            print("Please enter a valid number of parking hours")

    else:
        print("Invalid vehicle type")

    # Validate user input: only accept 'y' or 'n'
    while True:
        cont = input("Do you want to continue? (y/n): ").lower()
        if cont in ['y', 'n']:
            break
        print("Invalid input. Please enter only 'y' or 'n'.")
    
    print("------------------------------")
    if cont == "n":
        print("VT\tHours\tCost")
        print(f"1\t{MTT:.2f}\t{MTF:.2f} THB")
        print(f"2\t{CTT:.2f}\t{CTF:.2f} THB")
        print(f"Total {(MTF + CTF):.2f} THB")
        break