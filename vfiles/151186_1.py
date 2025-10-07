price = input("Enter Price :")
price = float(price)
point = input("Enter point :")
point = int(point)
discount = int(point)/500
total = price - discount

print (f"Your discount is {discount:.2f}")
print (f"Total is {total:.2f}")