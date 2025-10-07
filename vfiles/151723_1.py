# dictionary รหัสสัตว์
code = {
    "Dog": 0,
    "Cat": 1,
    "Fish": 2,
}

# รับอินพุตจากผู้ใช้
text = input("Enter your pets: ") # เช่น Dog,Cat,Dog,Fish,Cat
pets = text.split(",")

# แปลงชื่อสัตว์เป็นรหัส
code = []
for i in pets:
    codes.append(code[i])

# แสดงรหัสสัตว์
print("Code of your pets:", end=" " )
for i in range(len(codes)):
    if i < len(codes) - 1:
        print(codes[i]), end=","
    else:
        print(codes[i])

 # สร้าง one-hot vector จากรหัส
print("One-hot vector:")
for c in codes:
    vector = [0, 0, 0]
    vector[c] = 1
    print(vector)