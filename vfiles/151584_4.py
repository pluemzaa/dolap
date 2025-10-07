price = input("Enter product price:")
point = input("Enter your point:")
discount = float(point)/500
total =float(price)-discount
print(f"{discount:.2f}")
print(f"{total:.2f} baht")