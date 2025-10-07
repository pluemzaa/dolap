def calculate_personal_income_tax():
    """
    Calculates the personal income tax based on the net income
    according to Thailand's progressive tax rates.
    """
    try:
        net_income = float(input("Please enter your net income: "))
    except ValueError:
        print("Invalid input. Please enter a numerical value for net income.")
        return

    if net_income < 0:
        print("Net income cannot be negative. Please enter a valid amount.")
        return

    tax_amount = 0.0

    if net_income <= 150000:
        tax_amount = 0
    elif net_income <= 300000:
        tax_amount = (net_income - 150000) * 0.05
    elif net_income <= 500000:
        tax_amount = ((net_income - 300000) * 0.10) + 7500
    elif net_income <= 750000:
        tax_amount = ((net_income - 500000) * 0.15) + 27500
    elif net_income <= 1000000:
        tax_amount = ((net_income - 750000) * 0.20) + 65000
    elif net_income <= 2000000:
        tax_amount = ((net_income - 1000000) * 0.25) + 115000
    elif net_income <= 5000000:
        tax_amount = ((net_income - 2000000) * 0.30) + 365000
    else:  # net_income > 5000000
        tax_amount = ((net_income - 5000000) * 0.35) + 1265000

    print(f"The tax amount you have to pay this year : {tax_amount:.2f}")

# Call the function to run the program
calculate_personal_income_tax()