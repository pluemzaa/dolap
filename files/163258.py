A = input("Membership (y/n) : ")
A = A.lower()
B = float(input("Total amount : "))
discount = 0

if A == "y":
      if B >= 1000:
            discount = B * 0.20
      elif 500 <= B <= 999:
            discount = B * 0.10
            
elif A == "n":
      if B >= 1000:
            discount = B * 0.05 

print(f"Discount : {discount:.2f}")
print(f"Final Amount to Pay : {B-discount:.2f}")