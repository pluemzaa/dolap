price = input("Enter product price: ")
price = float(price) 
point = input("Enter your point: ")
point = float(point)  
discount = (point) / 500
discount = float(discount)
total = price - discount
total = float(total)    
print(f"Discount: {discount:.2f}")
print(f"Total: {total:.2f} Baht")