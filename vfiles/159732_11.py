net_income = float(input("Please enter your net income: "))
tax = 0

if net_income <= 150000:
    tax = 0
elif net_income <= 300000:
    tax = (net_income - 150000) * 0.05
elif net_income <= 500000:
    tax = (150000 * 0.05) + (net_income - 300000) * 0.10
elif net_income <= 750000:
    tax = (150000 * 0.05) + (200000 * 0.10) + (net_income - 500000) * 0.15
elif net_income <= 1000000:
    tax = (150000 * 0.05) + (200000 * 0.10) + (250000 * 0.15) + (net_income - 750000) * 0.20
elif net_income <= 2000000:
    tax = (150000 * 0.05) + (200000 * 0.10) + (250000 * 0.15) + (250000 * 0.20) + (net_income - 1000000) * 0.25
elif net_income <= 5000000:
    tax = (150000 * 0.05) + (200000 * 0.10) + (250000 * 0.15) + (250000 * 0.20) + (1000000 * 0.25) + (net_income - 2000000) * 0.30
else:
    tax = (150000 * 0.05) + (200000 * 0.10) + (250000 * 0.15) + (250000 * 0.20) + (1000000 * 0.25) + (3000000 * 0.30) + (net_income - 5000000) * 0.35

print(f"The tax amount you have to pay this year: {tax:,.2f} THB")