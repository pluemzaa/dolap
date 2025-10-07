net_m = int(input("Please enter your net income: "))
if net_m >= 0:
    tax = (net_m - 0)*0.00  
    if net_m >=150001:
        tax = (net_m - 150000)*0.05 
        if net_m >=300001:
            tax = (net_m - 300000)*0.10 + 7500
            if net_m >=500001:
                tax = (net_m - 500000)*0.15 + 27500   
                if net_m >=750001:
                    tax = (net_m - 750000)*0.20 + 65000
                    if net_m >=1000001:
                        tax = (net_m - 1000000)*0.25 + 115000
                        if net_m >=2000001:
                            tax = (net_m - 2000000)*0.30 + 365000
                            if net_m >=5000001:
                                tax = (net_m - 5000000)*0.35 + 1265000
print(f"The tax amount you have to pay this year : {tax:.2f}")