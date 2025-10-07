Member = input("Membership (y/n) : ")
TolAm = int(input("Total amount : "))
if Member == "n" and TolAm > 999:
    D = (5/100)*TolAm
elif Member == "y" and TolAm > 999:
    D = (20/100)*TolAm
elif Member == "y" and TolAm < 1000 and TolAm > 499:
    D = (10/100)*TolAm
else:
    D = 0
Finalp = TolAm - D
print(f"Discount : {D:.2f}")
print("Final Amount to Pay :",f"{Finalp:.2f}")