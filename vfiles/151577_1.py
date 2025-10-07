price = input("Enter product price: ")
price = float(price)
point = 1/500 * price
print(point)
print("Your point: %.2f point" % point)
print(f"Total price (price:.2f), your point: {point:.2f} Baht")