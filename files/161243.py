total = 0.0
ve_1 = 0
ve_2 = 0
vc_1 = 0
vc_2 = 0


while True:
    h_type = int(input("Please enter vehicle type (1: Motorcycle, 2: Personal Car): "))
    hours= float(input("Please enter the number of parking hours: "))
    if hours > 0:
        if h_type in [1,2]:
                if(hours >= 1):
                    if h_type == 1:
                        fee = 10.0 + (5.0*(hours-1))
                        vc_1 += fee
                        ve_1 += hours
                    else:
                        fee = 30.0 + (15.0*(hours-1))
                        vc_2 += fee
                        ve_2 += hours
                else:
                    if h_type == 1:
                        fee = 0.0
                        vc_1 += fee
                        ve_1 += hours
                    else:
                        fee = 0.0
                        vc_2 += fee
                        ve_2 += hours

                total += fee

               
                print(f"Parking fee: {fee:.2f} THB")
        else:
            print("Invalid vehicle type")
    else:
        
        print("Please enter a valid number of parking hours")

    check = input("Do you want to continue? (y/n): ")
    if check == 'n':
        print("------------------------------ ")
        print("VT Hours Cost")
        if ve_1 > 0:
            print(f"1 {ve_1:.2f} {vc_1:.2f}")

        if ve_2 > 0:
            print(f"2 {ve_2:.2f} {vc_2:.2f}")

            
        print(f"Total {total:.2f} THB")
        break
    
    else:
        print("------------------------------ ")