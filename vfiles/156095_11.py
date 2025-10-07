key_number = int(input("Enter key"))
text1 = "hello"
text2 = ""

letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m',
           'n','o','p','q','r','s','t','u','v','w','x','y','z']

for letter in text1:
    new = (letters.index(letter) + key_number) % 26
    text2 = text2 + letters[new]

print("Cipher of", text1, "is", text2)