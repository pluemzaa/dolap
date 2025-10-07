# รับรายได้สุทธิจากผู้ใช้
net_income = float(input("Please enter your net income: "))

# ตัวแปรภาษีเริ่มต้น
tax = 0

# ลำดับขั้นของภาษี (ช่วงรายได้, อัตราภาษี)
brackets = [
    (0, 150000, 0.00),
    (150000, 300000, 0.05),
    (300000, 500000, 0.10),
    (500000, 750000, 0.15),
    (750000, 1000000, 0.20),
    (1000000, 2000000, 0.25),
    (2000000, 5000000, 0.30),
    (5000000, float('inf'), 0.35)
]

# คำนวณภาษีแบบขั้นบันได
for lower, upper, rate in brackets:
    if net_income > lower:
        taxable = min(net_income, upper) - lower
        tax += taxable * rate

# แสดงผลลัพธ์
print(f"The tax amount you have to pay this year: {tax:,.2f}")