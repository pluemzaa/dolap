listhour = []
listprice = []
listcar = []


while True : 
    car = int(input("Please enter vehicle type (1: Motorcycle, 2: Personal Car):"))
    hour =float(input("Please enter the number of parking hours:")) 

    if car in [1,2] :
        listcar.append(car)

    if car != 1 and car != 2 :
        print("Invalid vehicle type")
    if hour <= 0 :
        print("Please enter a valid number of parking hours")
    
    
    if car == 1 and hour > 0 :
        if hour >0 and hour < 1:
            price = 0 
        elif hour == 1 : 
            price = 10 
        else : 
            price = ((hour - 1)*5) + 10
        listhour.append(hour)           
        listprice.append(price)
        print(f"Parking fee: {price:.2f} THB")
    
    if car == 2 and hour > 0 : 
        if hour >0 and hour < 1:
            price = 0 
        elif hour == 1 : 
            price = 30 
        else : 
            price = ((hour - 1)*15) + 30
        listhour.append(hour)           
        listprice.append(price) 
        print(f"Parking fee: {price:.2f} THB")
    
    
    
    cont = input("Do you want to continue? (y/n):")
    if cont == 'n' :
          break
    else :
        print("------------------------------")

print("------------------------------")
print("VT Hours Cost")


for i in range(len(listprice)) : 
        print(f"{listcar[i]:} {listhour[i]:.2f} {listprice[i]:.2f}") 
print(f"Total {sum(listprice):.2f} THB")