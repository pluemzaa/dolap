c1 = 0
totalft = 0
totalfe = 0
timees = 0
timeed = 0
while True:
    menu = int(input("Please enter vehicle type (1: Motorcycle, 2: Personal Car): "))
    time = float(input("Please enter the number of parking hours: "))
    if 0 < time:
        if menu == 1:
            if time < 1:
                total = 0
                print(f"Parking fee: {total:.2f} THB")
            else:
                timeed += time
                f = time - 1
                gg = 10
                tot = f * 5
                total = tot + gg
                print(f"Parking fee: {total:.2f} THB")
                totalft += total
                
        elif menu == 2:
            if time < 1:
                total = 0
                print(f"Parking fee: {total:.2f} THB")
            else:
                timees += time
                f = time - 1
                gg = 30
                tot = f * 15
                total = tot + gg
                print(f"Parking fee: {total:.2f} THB")
                totalfe += total

        else:
            print("Invalid vehicle type")
    else:
        print("Please enter a valid number of parking hours")
        
    cont = input("Do you want to continue? (y/n): ")
    if cont == 'n':
        break
    print("------------------------------")
        
        
alltotal = totalfe + totalft
print("VT Hours Cost")
print(f"1 {timeed:.2f} {totalft:.2f}")
print(f"2 {timees:.2f} {totalfe:.2f}")
print(f"Total {alltotal:.2f} THB")