# นปโปะมีร้านค้า นปโปะเห็นว่าช่วงนี้ร้านขายของไม่ค่อยได้ จึงคิดโปรโมชั่นเรียกลูกค้า นั่นคือ ถ้าซื้อถึงยอดที่กำหนดจะลดราคาตามเงื่อนไข และถ้าลูกค้าเป็นสมาชิก จะมีส่วนลดพิเศษให้ต่างหาก นปโปะต้องสร้างโปรแกรมคำนวณราคาให้พนักงานร้านนปโปะ 
# เงื่อนไขมีดังนี้
# -    หากลูกค้าเป็นสมาชิก และมีซื้อสินค้า 1000 บาทขึ้นไป จะได้ส่วนลด 20%
# -    หากลูกค้าเป็นสมาชิก และมีซื้อสินค้า 500 – 999 บาท จะได้ส่วนลด 10%
# -    หากลูกค้าไม่ได้เป็นสมาชิก และมีซื้อสินค้า 1000 บาทขึ้นไป จะได้ส่วนลด 5%
# -    หากซื้อไม่ถึงยอดที่กำหนด จะไม่ได้รับส่วนลดใดๆ

total = 0

user_in = input("Membership (y/n) : ")

if user_in == 'y':
    member = True
else:
    member = False

total = float(input("Total amount : "))

if member and total >= 1000:
    discount = total * 0.2
elif member and total >= 500:
    discount = total * 0.1
elif not member and total >= 1000:
    discount = total * 0.05
else:
    discount = 0

print(f"Discount : {discount:.2f}")
print(f"Final Amount to Pay : {total-discount:.2f}")

# discount