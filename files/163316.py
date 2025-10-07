m = (input("Membership (y/n):"))
ta = int(input("Total amount:"))

if m == ("y"):
     if ta >= 1000:
          discount = (ta*20)/100
     else:
          discount = (ta*10)/100
          
if m == ("n"):
     if ta >= 1000:
          discount = (ta*5)/100
     else:
          discount = 0
          
if ta < 500:
     discount = 0
     
print(f"Discount:{discount:.2f}")
total = ta - discount
print(f"Final Amount to Pay:{total:.2f}")