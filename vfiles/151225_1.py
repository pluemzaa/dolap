price = input("Enter product price: ")
point = input("Enter your point: ")
price = float(price)
Discount = 1/500 * price
Total = price - Discount 

print(f"Discount:{Discount:.2f}")
print(f"Total:{Total:.2f} Baht")