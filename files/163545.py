membership = input("Membership (y/n) : ").strip().lower()
total_amount = float(input("Total amount : "))


discount = 0.0


if membership == "y":  
    if total_amount >= 1000:
        discount = total_amount * 0.20
    elif 500 <= total_amount <= 999:
        discount = total_amount * 0.10
elif membership == "n":  
    if total_amount >= 1000:
        discount = total_amount * 0.05


final_amount = total_amount - discount

print(f"Discount : {discount:.2f}")
print(f"Final Amount to Pay : {final_amount:.2f}")