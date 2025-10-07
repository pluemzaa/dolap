inc = int(input("Please enter your net income:"))
tax = float()

if inc <= 150000:
    tax = 0
elif 150001 <= inc <= 300000:
    tax = (inc - 150000) * 0.05
elif 300001 <= inc <= 500000:
    tax = (inc - 300000) * 0.10 + 7500
elif 500001 <= inc <= 750000:
    tax = (inc - 500000) * 0.15 + 27500
elif 750001 <= inc <= 1000000:
    tax = (inc - 750000) * 0.20 + 65000
elif 1000001 <= inc <= 2000000:
    tax = (inc - 1000000) * 0.25 + 115000
elif 2000001 <= inc <= 5000000:
    tax = (inc - 2000000) * 0.30 + 365000
elif inc > 5000000:
    tax = (inc - 5000000) * 0.35 + 1265000

print(f"The tax amount you have to pay this year : {tax:.2f} ")