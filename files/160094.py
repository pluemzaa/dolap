c = float(input("Please enter your net income:"))
tax = 0

if c <= 150000:
    tax = 0
elif c <= 300000:
    tax = (c- 150000) * 0.05
elif c<= 500000:
  
    tax = ((c- 300000) * 0.10) + 7500
elif c<= 750000:
    
    tax = ((c- 500000) * 0.15) + 27500
elif c<= 1000000:
    
    tax = ((c- 750000) * 0.20) + 65000
elif c<= 2000000:
    
    tax = ((c- 1000000) * 0.25) + 115000
elif c<= 5000000:
    
    tax = ((c- 2000000) * 0.30) + 365000
else:
    tax = ((c- 5000000) * 0.35) + 1265000
print(f"The tax amount you have to pay this year: {tax:.2f} ")