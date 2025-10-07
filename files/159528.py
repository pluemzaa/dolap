income = int(input("Please enter your net income:"))


if 0 <= income <= 150000 :
        price = 0
        print(f"The tax amount you have to pay this year : {price:.2f} ") 
elif 150000 < income <= 300000 :
        price = (income - 150000) * 0.05
        print(f"The tax amount you have to pay this year : {price:.2f} ") 
elif 300000 < income <= 500000 :
        price = ((income - 300000) * 0.10) + 7500
        print(f"The tax amount you have to pay this year : {price:.2f} ")
elif 500000 <= income <= 750000 :
        price = ((income - 500000) * 0.15) + 27500
        print(f"The tax amount you have to pay this year : {price:.2f} ")
elif 750000 < income <= 1000000 :
        price = ((income - 750000) * 0.20) + 65000
        print(f"The tax amount you have to pay this year : {price:.2f} ")
elif 1000000 < income <= 2000000 :
        price = ((income - 1000000) * 0.25) + 115000
        print(f"The tax amount you have to pay this year : {price:.2f} ")
elif 2000000 < income <= 5000000 :
        price = ((income - 2000000) * 0.30) + 365000
        print(f"The tax amount you have to pay this year : {price:.2f} ")
else :
        price = ((income - 5000000) * 0.35) + 1265000
        print(f"The tax amount you have to pay this year : {price:.2f} ")