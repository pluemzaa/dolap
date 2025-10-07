price = input("Enter product price: ")
point = input("Enter your point: ")
discount = point/500
total = price - discount

print (f"Your discount is {discount:.2f}")
print (f"Total is {total:.2f}")