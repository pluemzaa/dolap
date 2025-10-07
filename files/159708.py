ni = int(input("Please enter your net income:"))

t = -1

if ni > 0 and ni <= 150000:
    t = 0
elif ni <= 300000:
    t = (ni-150000)*0.05
elif ni <= 500000:
    t = (ni-300000)*0.1 + 7500
elif ni <= 750000:
    t = (ni-500000)*0.15 + 27500
elif ni <=1000000:
    t = (ni-750000)*0.2 + 65000
elif ni <= 2000000:
    t = (ni-1000000)*0.25 + 115000
elif ni <= 5000000:
    t = (ni-2000000)*0.3 + 365000
else:
    t = (ni-5000000)*0.35 + 1265000
print(f"The tax amount you have to pay this year : {t:.2f}")