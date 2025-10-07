price = input("Enter product price: ")
point = input("Enter your point: ")
price = float(price)
point = int(point)

discount = point/500 
total = price - discount

print(f"Enter product price: {price:.2f}")
print(f"Enter your point: {point}")
print(f"Discount: {discount:.2f}")
print(f"Total: {total:.2f} Bath")