price = float(input("Enter product price: "))
point = int(input("Enter your point: "))
Discount = point/500 
total("Your point: %.2f point" % point)
total(f"Total price {price:.2f} , Your point: {point: .2f} point")