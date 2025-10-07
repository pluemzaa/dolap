type = int(input("Please enter vehicle type (1: Motorcycle, 2: Personal Car): "))
park_time1 = 0
park_time2 = 0
fee1 = 0
fee2 = 0



if type == 1 :
    park_time1 = float(input("Please enter the number of parking hours: "))
    if park_time1 < 0:
     print("Please enter a valid number of parking hours")
    elif park_time1 < 1 :
        fee1 = 0
        print(f"Parking fee: {fee1:.2f} THB")
    elif park_time1 <= 1 :
        fee1 = 10*park_time1 ; 
        print(f"Parking fee: {fee1:.2f} THB")
    elif park_time1 > 1:
        fee1 = (5 * (park_time1-1)) + 10
        print(f"Parking fee: {fee1:.2f} THB")
    
if type == 2 :
    park_time2 = float(input("Please enter the number of parking hours: "))
    if park_time2 < 0:
     print("Please enter a valid number of parking hours")
    elif park_time2 < 1 :
        fee2 = 0
        print(f"Parking fee: {fee2:.2f} THB")
        print("Do you want to continue? (y/n):")
    elif park_time2<= 1 :
        fee2 = 30 * park_time2 ; 
        print(f"Parking fee: {fee2:.2f} THB")
        print("Do you want to continue? (y/n):")
    elif park_time2 > 1:
            fee2 = (15 * (park_time2-1) + 30);
            print (f"Parking fee: {fee2:.2f} THB")
elif type > 2 : 
    print("Invalid vehicle type")





ans = input("Do you want to continue? (y/n): ")
print("------------------------------")


while ans == ("y"):
    type = int(input("Please enter vehicle type (1: Motorcycle, 2: Personal Car): "))
    

    if type == 1 :
        
        park_time1 = float(input("Please enter the number of parking hours: "))
        if park_time1 < 0:
            print("Please enter a valid number of parking hours")
            ans = input("Do you want to continue? (y/n): ")
            print("------------------------------")
            break
        elif park_time1 < 1 :
            fee1 = 0
            print(f"Parking fee: {fee1:.2f} THB")
            ans = input("Do you want to continue? (y/n): ")
            print("------------------------------")
        elif park_time1 <= 1 :
            fee1 = 10*park_time1 ; 
            print(f"Parking fee: {fee1:.2f} THB")
            ans = input("Do you want to continue? (y/n): ")
            print("------------------------------")
        elif park_time1 > 1:
            fee1 = (5 * (park_time1-1)) + 10
            print(f"Parking fee: {fee1:.2f} THB")
            ans = input("Do you want to continue? (y/n): ")
            print("------------------------------")


    
    if type == 2 :
    
        park_time2 = float(input("Please enter the number of parking hours: "))
        if park_time2 < 0:
            print("Please enter a valid number of parking hours")
            ans = input("Do you want to continue? (y/n): ")
            print("------------------------------")
        elif park_time2 < 1 :
            fee2 = 0
            print(f"Parking fee: {fee2:.2f} THB")
            ans = input("Do you want to continue? (y/n): ")
            print("------------------------------")
        elif park_time2<= 1 :
            fee2 = 30 * park_time2 ; 
            print(f"Parking fee: {fee2:.2f} THB")
            ans = input("Do you want to continue? (y/n): ")
            print("------------------------------")
        elif park_time2 > 1:
            fee2 = (15 * (park_time2-1) + 30);
            print(f"Parking fee: {fee2:.2f} THB")
            ans = input("Do you want to continue? (y/n): ")
            print("------------------------------")


    elif type != ("1","2"):
        print("Invalid vehicle type")
        break


while ans == ("n"):
    print("VT Hours Cost")
    print(f"1 {park_time1:.2f} {fee1:.2f}")
    print(f"2 {park_time2:.2f} {fee2:.2f}")
    print("Total ",fee1 + fee2 ," THB")
    break

    break