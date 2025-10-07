price = float(input("Enter product price: "))
point = float(input("Enter your point: "))
discount = 1/500*point
print("Discount: ",discount)
total = price - discount
print(f"Total: {total:.2f} Haht")