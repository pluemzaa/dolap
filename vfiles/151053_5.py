price = input("Enter prodct price:")
point = input("Enter your point:")
price = float(price)
discount = point/500
print("Discount: %.2f" % discount)
print(f"Total price: {price:.2f} - {discount} bath")