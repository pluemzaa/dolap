c1 = 0
c2 = 0
p1 = 0
p2 = 0
while True:
    menu = int(input("Please enter vehicle type (1: Motorcycle, 2: Personal Car): "))
    time = float(input("Please enter the number of parking hours: "))
    if 0 < time:
        if menu == 1:
            f = time - 1
            gg = 10
            tot = f * 5
            total = tot + gg
            print(f"Parking fee: {total:.2f} THB")
            
        elif menu == 2:
            f = time - 1
            gg = 30
            tot = f * 15
            total = tot + gg
            print(f"Parking fee: {total:.2f} THB")

        else:
            print("Invalid vehicle type")
        print("------------------------------")
        cont = input("continue y/n: ")
        if cont == 'n':
            break