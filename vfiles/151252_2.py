# Enter product price: 1250.50
# Enter your point: 15200
# Discount: 30.40
# Total: 1220.10 Baht

price=float(input("enter product price:"))
point=int(input("enter your point:"))

DC = (point/500)
Realprice = price - DC

print(f"Discount{DC:.2f}")
print(f"Total:{Realprice:.2f}Baht")

# print("discount:%.2f \nTotal: %.2f baht"%Realprice )