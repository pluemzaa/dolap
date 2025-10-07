s = float(input("Please enter vehicle type (1: Motorcycle, 2: Personal Car): "))
w = float(input("Please enter the number of parking hours: "))
price = 0
price1 = 0
while True:
    if s==1 :
        if w > 0:
            if w < 1 :
                price = 0 * w
                print(f"Parking fee:{price:.2f} THB")
            elif w == 1:
                price = 10 * w
                print(f"Parking fee:{price:.2f} THB")
            else:
                price =10+(w-1) * 5
                print(f"Parking fee:{price:.2f} THB")
        else:
            print("Please enter a valid number of parking hours")
    elif s==2 :
        if w > 0:
            if w < 1 :
                price1 = 0 * w
                print(f"Parking fee:{price1:.2f} THB")
            elif w == 1:
                price1 = 30 * w
                print(f"Parking fee:{price1:.2f} THB")
            else:
                price1 = 30 + (w-1) * 15
                print(f"Parking fee:{price1:.2f} THB")
        else:
            print("Please enter a valid number of parking hours")
    else :
        print("Invalid menu")
    con = input("Do you want to continue? (y/n):")
    if con=='n':
        break
print('VT Hours Cost')
print(s, w,price)
print(s, w,price1)
print(f"Total : {price1+price: .2f}")