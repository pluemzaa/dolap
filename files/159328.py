inc=float(input("Please enter your net income: "))
if inc <=150000:
    inc=x=0
    print(f"The tax amount you have to pay this year : {x:.2f}")
elif inc <=300000:
    x=(inc-150000) * 0.05
    print(f"The tax amount you have to pay this year : {x:.2f}")
elif inc <=500000:
    x=(inc-300000) * 0.1 + 7500
    print(f"The tax amount you have to pay this year : {x:.2f}")
elif inc <=750000:
    x=(inc-500000) * 0.15 + 27500
    print(f"The tax amount you have to pay this year : {x:.2f}")
elif inc <=1000000:
    x=(inc-750000) * 0.2 + 65000
    print(f"The tax amount you have to pay this year : {x:.2f}")
elif inc <=2000000:
    x=(inc-1000000) * 0.25 + 115000
    print(f"The tax amount you have to pay this year : {x:.2f}")
elif inc <=5000000:
    x=(inc-2000000) * 0.3 + 365000
    print(f"The tax amount you have to pay this year : {x:.2f}")
else :
    x=(inc-5000000) * 0.35 + 1265000
    print(f"The tax amount you have to pay this year : {x:.2f}")