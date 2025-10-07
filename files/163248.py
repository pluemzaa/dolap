print("Beverage List:")
print("1. Coffee - $2.5 - Quantity: 10")
print("2. Tea - $1.5 - Quantity: 0")
print("3. Juice - $3.0 - Quantity: 2")

drinks = {
    "1" : ["Coffee",2.5,10],
    "2" :  ["Tea",1.5,0],
    "3" :  ["Juice",3.0,2]
}
_num = int(input("Enter the number of the beverage you want to purchase: "))
_qan = int(input("Enter the quantity you want to purchase: "))
drink = drinks[str(_num)]
if (drink[2]) < _qan:
    print(f"Sorry, {drink[0]} is out of stock\n\n")
else:
    
    total = _qan * drink[1]
    print(f"You purchased {_qan} {drink[0]} for ${total}")
    print("Enjoy your drink!")