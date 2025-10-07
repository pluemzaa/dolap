price = input("Enter product price: ")
price = float(price)
point = input("Enter your point: ")
point = int(point)
Discount = 1/500 * point
print(f"Discount: {Discount:.2f} ")
Total = price-Discount
print (f"Total: {Total:.2f} Bath")