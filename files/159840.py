def calculate_tax():
    net_income_str = input("Please enter your net income: ")

    is_valid_input = True
    decimal_point_count = 0

    for char in net_income_str:
        if char == '.':
            decimal_point_count += 1
        elif not char.isdigit():
            is_valid_input = False
            break
    
    if not is_valid_input or decimal_point_count > 1 or net_income_str == "" or net_income_str == ".":
        print("Invalid input. Please enter a valid number for net income.")
        return
    
    net_income = float(net_income_str)

    tax = 0.0

    if net_income <= 150000:
        tax = 0
    elif net_income <= 300000:
        tax = (net_income - 150000) * 0.05
    elif net_income <= 500000:
        tax = ((net_income - 300000) * 0.10) + 7500
    elif net_income <= 750000:
        tax = ((net_income - 500000) * 0.15) + 27500
    elif net_income <= 1000000:
        tax = ((net_income - 750000) * 0.20) + 65000
    elif net_income <= 2000000:
        tax = ((net_income - 1000000) * 0.25) + 115000
    elif net_income <= 5000000:
        tax = ((net_income - 2000000) * 0.30) + 365000
    else:
        tax = ((net_income - 5000000) * 0.35) + 1265000

    print(f"The tax amount you have to pay this year : {tax:.2f}")

calculate_tax()