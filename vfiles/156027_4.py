alphabet = "abcdefghijklmnopqrstuvwxyz"
text = "hello"
key = int(input("Enter Key: "))
i0 = alphabet.index(text[0]) 
i1 = alphabet.index(text[1]) 
i2 = alphabet.index(text[2]) 
i3 = alphabet.index(text[3]) 
i4 = alphabet.index(text[4]) 

ch0 = alphabet[(i0+ key) % 26]
ch1 = alphabet[(i1+ key) % 26]
ch2 = alphabet[(i2+ key) % 26]
ch3 = alphabet[(i3+ key) % 26]
ch4 = alphabet[(i4+ key) % 26]

cipher = ch0+ch1+ch2+ch3+ch4

print("Cipher of", text , "is",cipher)