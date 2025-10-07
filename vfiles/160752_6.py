type_list = []
time_list = []
price_list = []

while True :
    type = int(input("Please enter vehicle type (1: Motorcycle, 2: Personal Car): "))
    time = float(input("Please enter the number of parking hours: "))
    price = float(0)

    if type not in [1,2] :
        print ("Invalid vehicle type")
    elif time <= 0 :
        print ("Please enter a valid number of parking hours")
    else :
        if type == 1 :
            if time < 1 :
                price = 0
            else :
                price = 10 + (time - 1) * 5
        elif type == 2:
            if time < 1:
                price = 0
            else:
                price = 30 + (time - 1) * 15

        print("Parking fee: %.2f THB" % price)
        type_list.append(type)
        time_list.append(time)
        price_list.append(price)

    con = input("Do you want to continue? (y/n): ")
    if con == "n" :
            break
    elif con == "y" :
            print ("------------------------------")
            continue
    
print ("------------------------------")
print ("VT Hours Cost")
total = 0
for i in range (0,len(type_list)) :
    total = total + price_list[i]
    print (type_list[i],('%.2f'%time_list[i]),('%.2f'%price_list[i]))

print ("Total %.2f THB"%total)