price = input("Enter product price:")
price = float(price)
point = input("Enter your point:")
point = float(point)
Discount = point/500 
Discount = float(Discount)
print (f"Discount: {Discount:.2f}")
Total = price-Discount
print (f"Total: {Total:.2f} Bath")