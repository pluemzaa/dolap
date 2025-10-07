parking = []

while True:
    v = input("Please enter vehicle type (1: Motorcycle, 2: Personal Car): ").strip()
    h = input("Please enter the number of parking hours: ").strip()


    i = (h.replace('.', '', 1).isdigit() and h.count('.') <= 1 and (h[0] != '-' or h == "0"))

    if not i:
        print("Please enter a valid number of parking hour")
    else:
        hours = float(h)
        if hours <= 0:
            print("Please enter a valid number of parking hour")
        elif v != '1' and v != '2':
            print("Invalid vehicle type")
        else:
            if hours < 1:
               cost = 0.0
            elif v == "1":
               cost = 10 + (hours - 1) * 5
            else:  
               cost = 30 + (hours - 1) * 15

            print("Parking fee: {:.2f} THB".format(cost))
            parking.append((v, hours, cost))

    cont = input("Do you want to continue? (y/n): ").strip().lower()
    print("------------------------------")
    if cont != 'y':
        break

print("VT Hours Cost")
total = 0.0
for vt, hr, fee in parking:
    print(f"{vt} {hr:.2f} {fee:.2f}")
    total += fee
print("Total {:.2f} THB".format(total))