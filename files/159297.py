"""
1. เงินได้สุทธิ 0 – 150,000 บาท (อัตราภาษี 0% หรือได้รับการยกเว้นภาษี)
    ภาษี = 0

2. เงินได้สุทธิ 150,001 – 300,000 บาท (อัตราภาษี 5%)
    ภาษี = (เงินได้สุทธิ – 150,000) x 5%

3. เงินได้สุทธิ 300,001 – 500,000 บาท (อัตราภาษี 10%)
   ภาษี = [ (เงินได้สุทธิ – 300,000) x 10% ] + 7,500

4. เงินได้สุทธิ 500,001 – 750,000 บาท (อัตราภาษี 15%)
   ภาษี = [ (เงินได้สุทธิ – 500,000) x 15% ] + 27,500
"""

income  = float(input("Please enter your net income: "))

if income > 5000000:
    print(f"The tax amount you have to pay this year : {((income-5000000)*0.35)+1265000:.2f}")
elif income > 2000000:
    print(f"The tax amount you have to pay this year : {((income-2000000)*0.30)+365000:.2f}")
elif income > 1000000:
    print(f"The tax amount you have to pay this year : {((income-1000000)*0.25)+115000:.2f}")
elif income > 750000:
    print(f"The tax amount you have to pay this year : {((income-750000)*0.20)+65000:.2f}")
elif income > 500000:
    print(f"The tax amount you have to pay this year : {((income-500000)*0.15)+27500:.2f}")
elif income > 300000:
    print(f"The tax amount you have to pay this year : {((income-300000)*0.1)+7500:.2f}")
elif income > 150000:
    print(f"The tax amount you have to pay this year : {((income-150000)*0.05):.2f}")
else:
    print(f"The tax amount you have to pay this year : 0.00")
# Please enter your net income: 15000
# The tax amount you have to pay this year : 0.00

# Please enter your net income: 200000
# The tax amount you have to pay this year : 2500.00