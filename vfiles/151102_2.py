product = input("Enter product price")
product = float(product)
point = input("Enter your point")
point = int(point)
Discount = point/500
Price = product- Discount
print(f"Discount: {Discount:.2f} \nTotal : {Price:.2f} Baht")