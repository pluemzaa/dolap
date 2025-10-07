Bever= ["Coffee","Tea","Juice"]
quan_list = [10,0,2]
print("""
Beverage List:
1. Coffee - $2.5 - Quantity: 10
2. Tea - $1.5 - Quantity: 0
3. Juice - $3.0 - Quantity: 2""")
baverage = input("Enter the number of the beverage you want to purchase: ")
quan = int(input("Enter the quantity you want to purchase: "))
if baverage == "2"  :
    print (f"Sorry, {Bever[1]} is out of stock")
if baverage == "1" :
    if quan > quan_list[0]:
        print (f"Sorry, {Bever[0]} is out of stock")
    else :
        print(f"You purchased {quan} Coffee for ${(quan*2.5):.1f}")
        print("Enjoy your drink!")
elif baverage == "3" :
    if quan > quan_list[2]:
        print (f"Sorry, {Bever[2]} is out of stock")
    else :
            print(f"You purchased {quan} Coffee for ${(quan*3.0):.1f}")
            print("Enjoy your drink!")