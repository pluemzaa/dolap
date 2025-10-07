oreo = [2.5,1.5,3.0]
you = ['Coffee','Tea','Juice']
re = [10,0,2]

yuu = int(input("Enter the number of the beverage you want to purchase: "))
tuu = int(input("Enter the quantity you want to purchase: "))
plo = yuu - 1
if re[plo] < tuu:
    print(f"Sorry, {you[plo]} is out of stock")
else:
    total = oreo[plo] * tuu
    print(f"You purchased {tuu} Coffee for ${total:.1f}")
    print("Enjoy your drink!")