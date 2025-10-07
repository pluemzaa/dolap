net = float(input("Please enter your net income:"))
if net >= 0 and net <= 150000 :
    print("The tax amount you have to pay this year : 0.00")
elif net >= 150001 and net <= 300000 :
    print(f"The tax amount you have to pay this year :{(net-150000)*0.05:.2f}")
elif net >= 300001 and net <= 500000 :
    print(f"The tax amount you have to pay this year :{((net-300000)*0.1)+7500:.2f}")
elif net >= 500001 and net <= 750000 :
    print(f"The tax amount you have to pay this year :{((net-500000)*0.15)+27500:.2f}")
elif net >= 750001 and net <= 1000000 :
    print(f"The tax amount you have to pay this year :{((net-750000)*0.2)+65000:.2f}")
elif net >= 1000001 and net <= 2000000 :
    print(f"The tax amount you have to pay this year :{((net-1000000)*0.25)+115000:.2f}")
elif net >= 2000001 and net <= 5000000 :
    print(f"The tax amount you have to pay this year :{((net-2000000)*0.3)+365000:.2f}")
else :
    print(f"The tax amount you have to pay this year :{((net-5000000)*0.35)+1265000:.2f}")