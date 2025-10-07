price = input("Enter product price: ")
point = int(input("Enter your point: "))
price = float(price)
Discount = 1/500 * point
result = price - Discount
print("Discount: " ,Discount)
total = price - Discount
print("Total: %.2f Baht" %total)