# นปโปะมีร้านค้า นปโปะเห็นว่าช่วงนี้ร้านขายของไม่ค่อยได้ จึงคิดโปรโมชั่นเรียกลูกค้า นั่นคือ ถ้าซื้อถึงยอดที่กำหนดจะลดราคาตามเงื่อนไข และถ้าลูกค้าเป็นสมาชิก จะมีส่วนลดพิเศษให้ต่างหาก นปโปะต้องสร้างโปรแกรมคำนวณราคาให้พนักงานร้านนปโปะ 

# เงื่อนไขมีดังนี้
# -    หากลูกค้าเป็นสมาชิก และมีซื้อสินค้า 1000 บาทขึ้นไป จะได้ส่วนลด 20%
# -    หากลูกค้าเป็นสมาชิก และมีซื้อสินค้า 500 – 999 บาท จะได้ส่วนลด 10%
# -    หากลูกค้าไม่ได้เป็นสมาชิก และมีซื้อสินค้า 1000 บาทขึ้นไป จะได้ส่วนลด 5%
# -    หากซื้อไม่ถึงยอดที่กำหนด จะไม่ได้รับส่วนลดใดๆ

# ตัวอย่างหน้าจอ #1

# Membership (y/n) : y
# Total amount : 1000

# Discount : 200.00
# Final Amount to Pay : 800.00

# ตัวอย่างหน้าจอ #2

# Membership (y/n) : y
# Total amount : 900

# Discount : 90.00
# Final Amount to Pay : 810.00

# ตัวอย่างหน้าจอ #3

# Membership (y/n) : n
# Total amount : 1000

# Discount : 50.00
# Final Amount to Pay : 950.00

# ตัวอย่างหน้าจอ #4

# Membership (y/n) : y
# Total amount : 300

# Discount : 0.00
# Final Amount to Pay : 300.00

mb = str(input('Membership (y/n) :'))
ta = float(input('Total amount :'))
ds = 0
fa = 0
if ta < 500:
    print("Discount : 0.00")
    print('Final Amount to Pay :',"%.2f"%ta)
elif mb is "y" and ta >= 1000:
    ds = (ta * 20)/100
    fa = ta - ds
    print("Discount :","%.2f"%ds)
    print('Final Amount to Pay :',"%.2f"%fa)
elif mb is "y" and ta < 1000 :
    ds = (ta * 10)/100
    fa = ta - ds
    print("Discount :","%.2f"%ds)
    print('Final Amount to Pay :',"%.2f"%fa)
    
elif mb is 'n' and ta >= 1000 :
    ds = (ta * 5)/100
    fa = ta - ds
    print("Discount :","%.2f"%ds)
    print('Final Amount to Pay :',"%.2f"%fa)
else:
    print("Discount : 0.00")
    print('Final Amount to Pay :',"%.2f"%ta)