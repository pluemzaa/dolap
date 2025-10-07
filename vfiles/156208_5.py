key = int(input("Enter key")) 
text = "hello"                 
result = ""                    

for ch in text:
    new_char = chr((ord(ch) - ord('a') + key) % 26 + ord('a'))
    result += new_char

print("Cipher of", text, "is", result)

print(f"Cipher of {text} is {text}")