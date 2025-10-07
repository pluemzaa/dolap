price = input("Enter product price:") 
price = float(price)

point = input("Enter your point:")
point = int(point)
point = 1/500 * point

pi = price-point

print("Discount:%.2f" % point)
print(f"Total:{pi:.2f} Baht")