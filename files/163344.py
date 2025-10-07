cp, cq = 2.5, 10
tp, tq = 1.5, 0
jp, jq = 3.0, 2

h = {1: [2.5, 10, 'Coffee'], 2: [1.5, 0, 'Tea'], 3: [3.0, 2, 'Juice']}

print("""Beverage List:
1. Coffee - $2.5 - Quantity: 10
2. Tea - $1.5 - Quantity: 0
3. Juice - $3.0 - Quantity: 2""")

b = int(input("Enter the number of the beverage you want to purchase: "))
q = int(input("Enter the quantity you want to purchase: "))
t = q*h[b][0]
if q > h[b][1]:
    print(f"Sorry, {h[b][2]} is out of stock")
else:
    print(f"You purchased {q} {h[b][2]} for ${t}\nEnjoy your drink!")