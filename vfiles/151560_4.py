price = float(input("Enter product price: "))
point = float(input("Enter your point: "))
Discount = point/500 
print("discount: {discount:%.2f}")
total = price-Discount
print("Total:{total:.2f} Baht")