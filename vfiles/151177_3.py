price = input("Enter product price:")
price = float(price)
point = input("Enter your point:")
point = float(point)
Discount = point/500 
Discount = float(Discount)
print ("Discount: %.2f" % Discount)
Total = price-Discount
print ("Total: %.2f Bath" % Total)