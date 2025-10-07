price = float(input("Enter product price: "))
point = int(input("Enter your point: "))
discount = point / 500
if discount > price:
    discount = price
  total = price - discount
print(f"Discount: {discount:.2f}")
print(f"Total: {total:.2f} Baht")