listhour1 = []
listhour2 = []
listprice = []
listcar = []
listmotor = []
c = 0
e = 0

while True : 
    car = int(input("Please enter vehicle type (1: Motorcycle, 2: Personal Car):"))
    hour = float(input("Please enter the number of parking hours:")) 

    

    if car not in [1,2] :
        print("Invalid vehicle type")
    if hour <= 0 :
        print("Please enter a valid number of parking hours")
    
    
    if car == 1 and hour > 0 :
        if hour < 1:
            price = 0 
        elif hour == 1 : 
            price = 10 
        else : 
            price = ((hour - 1)*5) + 10
        listmotor.append(price)
        listhour1.append(hour)           
        listprice.append(price)
        print(f"Parking fee: {price:.2f} THB")
        c += 1
    
    if car == 2 and hour > 0 : 
        if hour < 1:
            price = 0 
        elif hour == 1 : 
            price = 30 
        else : 
            price = ((hour - 1)*15) + 30
        listcar.append(price)
        listhour2.append(hour)           
        listprice.append(price) 
        print(f"Parking fee: {price:.2f} THB")
        e += 1
    
    
    cont = input("Do you want to continue? (y/n):")
    if cont == 'n' :
        break
    else:
        print("------------------------------")
        continue
    




if c > 0 and e > 0:
    print("------------------------------")
    print("VT Hours Cost") 
    print(f"1 {sum(listhour1):.2f} {sum(listmotor):.2f}")
    print(f"2 {sum(listhour2):.2f} {sum(listcar):.2f}")  
    print(f"Total {sum(listprice):.2f} THB")
elif c > 0 and e ==0 :
    print("------------------------------")
    print("VT Hours Cost") 
    print(f"1 {sum(listhour1):.2f} {sum(listmotor):.2f}") 
    print(f"Total {sum(listprice):.2f} THB")
elif c == 0 and e > 0:      
    print("------------------------------")
    print("VT Hours Cost") 
    print(f"2 {sum(listhour2):.2f} {sum(listcar):.2f}")   
    print(f"Total {sum(listprice):.2f} THB")