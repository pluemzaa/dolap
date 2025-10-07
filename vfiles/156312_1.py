def caesar_cipher(text, key):
    result = ’‘
    for char in text:
        if char.isalpha():  # ตรวจว่าตัวอักษรหรือไม่
            shift = ord(’a‘) if char.islower() else ord(’A‘)
            # ใช้สูตร Caesar Cipher
            encrypted = chr((ord(char) - shift + key) % 26 + shift)
            result += encrypted
        else:
            result += char  # ถ้าไม่ใช่ตัวอักษร ให้คงเดิม
    return result