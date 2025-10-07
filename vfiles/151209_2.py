price = int(input("Enter product price: "))
point = int(input("Enter your point: "))

price = float(price)
Discount = 500 / point
Total = price - Discount

print("Discount:" ,("%.2f" % Discount))
print("Total:" ,("%.2f Baht" % Total))