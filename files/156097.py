key = int(input("Enter key"))
text = "hello"
text = text.lower()
cipher = ""
for ch in text:

    if 'a' <= ch <= 'z':
        
        pos = ord(ch) - ord('a')
      
        new_pos = (pos + key) % 26
        
        new_char = chr(new_pos + ord('a'))
        
        cipher += new_char
    else:
        
        cipher += ch

print("Cipher of", text, "is", cipher)