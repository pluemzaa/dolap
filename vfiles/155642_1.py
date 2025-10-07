# Caesar Cipher Implementation

# ตัวอักษร a-z กับตำแหน่งที่เกี่ยวข้อง
char_map = {i: chr(97 + i) for i in range(26)}
reverse_char_map = {v: k for k, v in char_map.items()}

# รับค่าคีย์จากผู้ใช้
key_input = input("Enter key: ")
try:
    key = int(key_input)
except ValueError:
    print("Invalid key, must be an integer.")
    exit()

# ข้อความที่จะเข้ารหัส
text = "hello"
cipher_text = ""

for ch in text:
    if ch in reverse_char_map:
        original_index = reverse_char_map[ch]
        new_index = (original_index + key) % 26
        cipher_text += char_map[new_index]
    else:
        cipher_text += ch  # กรณีมีอักขระอื่นนอกจาก a-z

print(f"Cipher of {text} is {cipher_text}")