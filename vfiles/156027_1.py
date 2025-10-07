a ="abcdefghijklmnopqrstuvwxyz"
text = "hello"
key = 5
index0 =alphabet.index(text[0]) 
index1 =alphabet.index(text[1]) 
index2 =alphabet.index(text[2]) 
index3 =alphabet.index(text[3]) 
index4 =alphabet.index(text[4]) 

ch0 =alphabet[(index0+ ket)%26]
ch1 =alphabet[(index0+ ket)%26]
ch2 =alphabet[(index0+ ket)%26]
ch3 =alphabet[(index0+ ket)%26]
ch4 =alphabet[(index0+ ket)%26]
cipher = ch0+ch1+ch2+ch3+ch4
print("Cipher of", text , "is",cipher)