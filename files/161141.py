a = 0
b = 0
c = 0
v = 0
p = 0
r1 = 0
r2 = 0

while True:
    car = int(input("Please enter vehicle type (1: Motorcycle, 2: Personal Car): "))
    hour = float(input("Please enter the number of parking hours: "))

    if car != 1 and car != 2:
        print("Invalid vehicle type")
    elif car == 1:
        if hour <= 0:
            print("Please enter a valid number of parking hours")
        else:
            if hour > 0 and hour <= 1:
                z = 0
            elif hour > 1 and hour <= 2:
                z = 10
            elif hour > 2:
                z = 10 + ((hour - 1) * 5)
            c += hour
            a += z
            r1 += 1
            print("Parking fee: {:.2f} THB".format(z))
    elif car == 2:
        if hour <= 0:
            print("Please enter a valid number of parking hours")
        else:
            if hour > 0 and hour <= 1:
                z = 0
            elif hour > 1 and hour <= 2:
                z = 30
            elif hour > 2:
                z = 30 + ((hour - 1) * 15)
            v += hour
            b += z
            r2 += 1
            print("Parking fee: {:.2f} THB".format(z))

    con = input("Do you want to continue? (y/n): ")
    print("---------------------------------")
    if con == 'n':
        break

if r1 >= 1 or r2 >= 1:
    print