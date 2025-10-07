price = input("Enter product price: ")
point = int(input("Enter your point: "))
price = float(price)
Discount = 1/500 * point
print("Discount: %.2f" %Discount)
total = price - Discount
print("Total: %.2f Baht" %total)