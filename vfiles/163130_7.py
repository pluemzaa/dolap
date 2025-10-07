print("""Beverage List:
1. Coffee - $2.5 - Quantity: 10
2. Tea - $1.5 - Quantity: 0
3. Juice - $3.0 - Quantity: 2""")
c,t,j = 10,0,2
p1,p2,p3 = 2.5,1.5,3.0
dic = {1:"Coffee",2:"Tea",3:"Juice"}
x = int(input("Enter the number of the beverage you want to purchase: "))
y = int(input('Enter the quantity you want to purchase: '))
if x == 1:
    if c < y:
        print(f"Sorry, {dic[x]} is out of stock")
        print()
    else :
        print(f"You purchased {y} {dic[x]} for ${y*p1}")
        print('Enjoy your drink!')
elif x == 2:
    if t < y:
        print(f"Sorry, {dic[x]} is out of stock")
        print()
    else :
        print(f"You purchased {y} {dic[x]} for ${y*p2}")
        print('Enjoy your drink!')
elif x == 2:
    if j < y:
        print(f"Sorry, {dic[x]} is out of stock")
        print()
    else :
        print(f"You purchased {y} {dic[x]} for ${y*p3}")
        print('Enjoy your drink!')