price = input("Enter product price:") 
price = float(price)
point = 1/500 * price
print("Enter your point: %.2f" % point)
print(f"Discount: {point:.2f} , Total: {price:.2f} Baht")