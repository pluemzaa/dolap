total = 0
records = []
while True:
    menu = int(input("Please enter vehicle type (1: Motorcycle, 2: Personal Car): "))
    hours = float(input("Please enter the number of parking hours: "))

    if menu not in [1, 2]:
        print("Invalid vehicle type")
        break

    else:
        if hours <= 0:
            print("Please enter a valid number of parking hours")
            break

        else:
            if hours < 1:
                fee = 0
            
            elif menu == 1:
                fee = 10 + (hours - 1) * 5
            
            elif menu == 2:
                fee = 30 + (hours - 1) * 15
        print(f"Parking fee: {fee:.2f} THB")
        records.append([menu, hours, fee])
        total += fee


    cont = input("Do you want to continue? (y/n): ")
    print("------------------------------")
    if cont =='n':
        break


print("VT Hours Cost")
for record in records:
    print(f"{record[0]} {record[1]:.2f} {record[2]:.2f}")
print(f"Total {total:.2f} THB")