money = int(input("Please enter your net income: "))
if money<=150000:
    tex = 0
elif money <=300000:
    tex = (money-150000)*0.05
elif money <=500000:
    tex = ((money-300000)*0.1)+7500
elif money <=750000:
    tex = ((money-500000)*0.15)+27000
elif money <=1000000:
    tex = ((money-750000)*0.2)+65000
elif money <=2000000:
    tex = ((money-1000000)*0.25)+115000
elif money <=5000000:
    tex = ((money-2000000)*0.3)+365000
else:
    tex = ((money-5000000)*0.35)+1265000

print(f"The tax amount you have to pay this year : {tex:.2f}")