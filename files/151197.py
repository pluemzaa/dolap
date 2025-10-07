price = input("Enter product price:")
price = float(price)
point = input("Enter your point:")
point = int(point)
dis = 1/500 * point
print(f"Discount:{dis:.2f}") 
x= (price)-(dis)
print(f"Total:{x:.2f} Baht")