run = True
total1 = 0
total2 = 0
total = 0
hours1 = 0
hours2 = 0
while run:
    tay = int(input("Please enter vehicle type (1: Motorcycle, 2: Personal Car): "))
    hours = float(input("Please enter the number of parking hours: "))
    
    if tay == 1:
        if hours >= 1:
         
            fee1 = 10 + ((hours-1)*5)
            print(f"Parking fee: {fee1:.2f} THB")
            total1 = total1 + fee1
            hours1 = hours1 + hours
        elif hours > 0:

            fee1 = 0
            print(f"Parking fee: {fee1:.2f} THB")
            total1 = total1 + fee1
            hours1 = hours1 + hours
        else:
            print("Please enter a valid number of parking hours")
        


    elif tay == 2:
        if hours >= 1:
         
            fee2 = 30 + ((hours-1)*15)
            print(f"Parking fee: {fee2:.2f} THB")
            total2 = total2 + fee2
            hours2 = hours2 + hours
        elif hours > 0:

            fee2 = 0
            print(f"Parking fee: {fee2:.2f} THB")
            total2 = total2 + fee2
            hours2 = hours2 + hours
        else:
            print("Please enter a valid number of parking hours")
    
    else:
        print("Invalid vehicle type")
    
    
    x = input("Do you want to continue? (y/n):")

    if x == "n":
        run = False
    print("------------------------------ ( copy ไปเลย)")

total = total1 + total2
if hours1 == 0:

    print(f"""VT Hours Cost
    2 {hours2:.2f} {total2:.2f}
    Total {total:.2f} THB""")

elif hours2 == 0:
    print(f"""VT Hours Cost
    1 {hours1:.2f} {total1:.2f}
    Total {total:.2f} THB""")
else:

    print(f"""VT Hours Cost
    1 {hours1:.2f} {total1:.2f}
    2 {hours2:.2f} {total2:.2f}
    Total {total:.2f} THB""")