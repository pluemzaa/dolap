mt = 0   
ct = 0   
tt = 0   
mc = 0  
cc = 0  
t = 0
r = 0
while True:
    vt = int(input("Please enter vehicle type (1: Motorcycle, 2: Personal Car): "))
    hr = float(input("Please enter the number of parking hours: "))

    if vt <= 0 or vt > 2:
        print("Invalid vehicle type")
    elif vt == 1:
        if hr <= 0:
            print("Please enter a valid number of parking hours")
        else:
            if 0 < hr < 1:
                fee = 0
            if 1 <= hr < 2:
                fee = 10
            if hr >= 2:
                fee = 10 + ((hr - 1) * 5)

            mt += hr
            t += fee
            mc += 1
            print(f"Parking fee: {fee:.2f} THB")

    elif vt == 2:
        if hr <= 0:
            print("Please enter a valid number of parking hours")
        else:
            if 0 < hr < 1:
                fee = 0
            if 1 <= hr < 2:
                fee = 30
            if hr >= 2:
                fee = 30 + ((hr - 1) * 15)

            ct += hr
            r += fee
            cc += 2
            print(f"Parking fee: {fee:.2f} THB")

    yn = input("Do you want to continue? (y/n): ")
    print("------------------------------")
    if yn == 'n':
        break

if mc >= 1 or cc >= 1:
    print("VT Hours Cost")
    if mc >= 1:
        print(f"1  {mt:.2f}   {t:.2f}")
    if cc >= 1:
        print(f"2  {ct:.2f}   {r:.2f}")

tt = t + r
print(f"Total {tt:.2f} THB")