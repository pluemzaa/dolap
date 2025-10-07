price = input("Enter product price:")
price = float(price)
point = int(input("Enter your point"))
discount = point / 500
print(discount)
total = price - discount
print("Discount : %.2f" % discount)
print(f"Total {total:.2f} baht")