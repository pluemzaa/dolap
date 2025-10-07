# รับราคาสินค้าและแต้มสะสมจากผู้ใช้
price = float(input("Enter product price: "))
point = int(input("Enter your point: "))

# คำนวณส่วนลดจากแต้ม (500 แต้ม = 1 บาท)
discount = point / 500

# ห้ามให้ส่วนลดมากกว่าราคาสินค้า
if discount > price:
    discount = price

# คำนวณราคารวมหลังหักส่วนลด
total = price - discount

# แสดงผลลัพธ์ให้มีทศนิยม 2 ตำแหน่ง
print(f"Discount: {discount:.2f}")
print(f"Total: {total:.2f} Baht")