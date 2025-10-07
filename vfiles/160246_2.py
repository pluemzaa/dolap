t1 = 0
t2 = 0
s1 = 0
s2 = 0
while True:
    t = int(input("Please enter vehicle type (1: Motorcycle, 2: Personal Car): "))
    price = 0
    if t == 1 :
        pt = float(input("Please enter the number of parking hours: "))
        if pt > 0:
            if pt <1 :
                price = 0
                s1+=price
                t1+=pt
                print(f"Parking fee: {price:.2f} THB")
            elif pt == 1:
                price = 10
                s1+=price
                t1+=pt
                print(f"Parking fee: {price:.2f} THB")
            elif pt > 1:
                price = 10
                price = price+((pt-1)*5)
                s1+=price
                t1+=pt
                print(f"Parking fee: {price:.2f} THB") 
        else :
            print("Please enter a valid number of parking hours")
    elif t == 2 :
        pt = float(input("Please enter the number of parking hours: "))
        if pt > 0:
            if pt <1 :
                price = 0
                s2+=price
                t2+=pt
                print(f"Parking fee: {price:.2f} THB")
            elif pt == 1:
                price = 30
                s2+=price
                t2+=pt
                print(f"Parking fee: {price:.2f} THB")
            elif pt > 1:
                price = 30
                price = price+((pt-1)*15)
                s2+=price
                t2+=pt
                print(f"Parking fee: {price:.2f} THB")
        else :
            print("Please enter a valid number of parking hours") 
    else :
        print("Invalid vehicle type")
    con = input("Do you want to continue? (y/n): ")
    if con == "n":
        break
    elif con == "y" :
        print("------------------------------") 
        continue
    else :
       pass 
sum = s1+s2
print("VT Hours Cost")
print(f"1 {t1:.2f} {s1:.2f}")
print(f"2 {t2:.2f} {s2:.2f}")