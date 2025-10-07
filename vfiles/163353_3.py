print("Beverage List:")
print("1. Coffee - $2.5 - Quantity: 10")
print("2. Tea - $1.5 - Quantity: 0")
print("3. Juice - $3.0 - Quantity: 2")

type=int(input("Enter the number of the beverage you want to purchase: "))
quan=int(input("Enter the quantity you want to purchase: "))

if type==1:
    if quan<=10:
        tol=2.5*quan
        print(f"Enter the quantity you want to purchase:{tol}")
    else:
        Sorry, Tea is out of stock