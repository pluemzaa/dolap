price = float(input("Enter product price:"))
point = int(input("Enter your point:"))

dis = 1/500 * point
total = price - dis

print("Discount:",dis)
print(f"Total: {total:.2f} Bath")