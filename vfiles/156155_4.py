key = int(input("Enter key"))
text1 = "hello"
text2 = ""
letter = ['a','b','c','d','e','f','g','h','i','j','k','l','m',
           'n','o','p','q','r','s','t','u','v','w','x','y','z']
for letter in message1:
    position = letters.index(letter)
    new_position = (position + key_number) % 26
    new_letter = letters[new_position]
    text2 =text2 + new_letter
print("Cipher of", text1, "is", text2)