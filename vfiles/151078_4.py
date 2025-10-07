price = input("Enter product price: ")
price = float(price)
point = int(input("Enter your point: "))
discout = point/500
total = price-discout
print("Discount: ", discout)
print(f"Total: {total:.2f} Baht")