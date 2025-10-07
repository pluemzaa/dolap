# 1. เงินได้สุทธิ 0 – 150,000 บาท (อัตราภาษี 0% หรือได้รับการยกเว้นภาษี)
#     ภาษี = 0
# 2. เงินได้สุทธิ 150,001 – 300,000 บาท (อัตราภาษี 5%)
#     ภาษี = (เงินได้สุทธิ – 150,000) x 5%
# 3. เงินได้สุทธิ 300,001 – 500,000 บาท (อัตราภาษี 10%)
#    ภาษี = [ (เงินได้สุทธิ – 300,000) x 10% ] + 7,500
# 4. เงินได้สุทธิ 500,001 – 750,000 บาท (อัตราภาษี 15%)
#    ภาษี = [ (เงินได้สุทธิ – 500,000) x 15% ] + 27,500
# 5. เงินได้สุทธิ 750,001 – 1 ล้านบาท (อัตราภาษี 20%)
#    ภาษี = [ (เงินได้สุทธิ – 750,000) x 20% ] + 65,000
# 6. เงินได้สุทธิ 1,000,001 – 2,000,000 บาท (อัตราภาษี 25%)
#    ภาษี = [ (เงินได้สุทธิ – 1,000,000) x 25% ] + 115,000
# 7. เงินได้สุทธิ 2,000,001 – 5,000,000 บาท (อัตราภาษี 30%)
#    ภาษี = [ (เงินได้สุทธิ – 2,000,000) x 30% ] + 365,000
# 8. เงินได้สุทธิมากกว่า 5 ล้านบาท (อัตราภาษี 35%)
#    ภาษี = [ (เงินได้สุทธิ – 5,000,000) x 35% ] + 1,265,000

income = int(input("Please enter your net income: "))
tax = 0
if income <= 150000:
    tax = 0
    print(f"The tax amount you have to pay this year :{tax:.2f}")
elif income <= 300000:
    tax = (income - 150000)*(5/100)
    print(f"The tax amount you have to pay this year :{tax:.2f}")
elif income <= 500000:
    tax = (income - 300000)*(10/100)+ 7500
    print(f"The tax amount you have to pay this year :{tax:.2f}")
elif income <= 750000:
    tax = (income - 500000)*(15/100)+ 27500
    print(f"The tax amount you have to pay this year :{tax:.2f}")
elif income <= 1000000:
    tax = (income - 750000)*(20/100)+ 65000
    print(f"The tax amount you have to pay this year :{tax:.2f}")
elif income <= 2000000:
    tax = (income - 1000000)*(25/100)+ 115000
    print(f"The tax amount you have to pay this year :{tax:.2f}")
elif income <= 5000000:
    tax = (income - 2000000)*(30/100)+365000
    print(f"The tax amount you have to pay this year :{tax:.2f}")
else: 
    tax = (income - 5000000)*(35/100)+1265000
    print(f"The tax amount you have to pay this year :{tax:.2f}")