product_price= float(input("enter product price:"))
your_point=float(input("enter your point:"))
discount= your_point/500
total_price=product_price-discount
print(f"discount:{discount:.2f}")
print(f"Tontal:{total_price:.2F}Baht")