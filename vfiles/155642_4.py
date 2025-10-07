# Dictionary ของตัวอักษรตามลำดับ
alphabet = {i: chr(97 + i) for i in range(26)}  # 97 = 'a'
reverse_alphabet = {v: k for k, v in alphabet.items()}

# รับค่า key
key = int(input("Enter key: "))

# ข้อความต้นฉบับ
text = "hello"
cipher = ""

for char in text:
    index = reverse_alphabet[char]               # หาตำแหน่งของตัวอักษร
    new_index = (index + key) % 26                # Caesar formula
    cipher += alphabet[new_index]                # แปลงกลับเป็นตัวอักษร

print("Cipher of", text, "is", cipher)