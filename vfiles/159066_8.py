w = float(input("Enter weight: "))
s = int(input("Select service: "))
price = 0
if s==1:
    if w <= 5:
        price = 20
    elif w<=10:
         price = 18  
    else:
        price = 15
    price = price * w    
    print(f"Washing cost: {price:.2f}")

elif s==2:
    if w <= 5:
        price = 10
    elif w <= 10:
         price = 8  
    else:
        price = 7
    price = price * w
    print(f"Drying cost: {price:.2f}")

else:
    print("Invalid service")