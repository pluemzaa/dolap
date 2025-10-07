price = input("Enter product price:")
point = input("Enter your point:")
point = float(point)
price = float(price)
Discount = 1/500 * point
Discount = float(Discount)
print(Discount)
Total   = price - Discount
Total   = float(Total)
print(Total)
print("Discount: %.2f" % Discount)
print("Total: %.2f Baht" % Total)
#Enter product price: 1250.50
#Enter your point: 15200
#Discount: 30.40
#Total: 1220.10 Baht