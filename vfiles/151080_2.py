price = input("Enter product price: ")
point = input("Enter your point: ")
price = float(price)
point = int(point)
discout = point/500
total = price - discout

print(f"Enter product price: {price:.2f} \n Enter you point: {point:.2f} \n Discount: {discout:.2f} \n Total: {total:.2f} Baht")