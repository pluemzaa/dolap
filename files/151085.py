price = input("Enter product price:")
price = float(price)
point = 1/500*float(price)
point = input("Enter your point:")
Discount = 1/500*float(point)
print("Discount: %.2f " %Discount)
total = price-Discount
print("Total: %.2f Baht " %total)