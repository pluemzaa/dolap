w = float(input("Please enter your net income:"))
a = 0
if w<=150000:
    print("The tax amount you have to pay this year : 0.00")
elif w<=300000:
     a = (w-150000)*0.05
     print(f"The tax amount you have to pay this year :{a:.2f}")
elif w<=500000:
     a = ((w-300000)*0.1)+7500
     print(f"The tax amount you have to pay this year :{a:.2f}")
elif w<=750000:
     a = ((w-500000)*0.15)+27500
     print(f"The tax amount you have to pay this year :{a:.2f}")
elif w<=1000000:
     a = ((w-750000)*0.2)+65000
     print(f"The tax amount you have to pay this year :{a:.2f}")
elif w<=5000000:
     a = ((w-2000000)*0.3)+365000
     print(f"The tax amount you have to pay this year :{a:.2f}")
else:
     a = ((w-5000000)*0.35)+1265000
     print(f"The tax amount you have to pay this year :{a:.2f}")