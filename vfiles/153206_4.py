data = {0: 'a', 1: 'b', 2: 'c', 3: 'd', 4: 'e', 5: 'f', 6: 'g', 7: 'h', 8: 'i', 9: 'j', 10: 'k', 11: 'l', 12: 'm', 13: 'n', 14: 'o', 15: 'p', 16: 'q', 17: 'r', 18: 's', 19: 't', 20: 'u', 21: 'v', 22: 'w', 23: 'x', 24: 'y', 25: 'z'}
data2 = {}
hello = 7 ,4 ,11 ,11 ,14 
a = 0
b = str()
key = input('Enter key')
#Caesar_cipher = ( b[] + key ) % 26
#แปลงเป็นตัวอักษรเพื่่อที่จะนำมา + กัน 

while a <= 4 :
    hello_1 = ( hello[a] + int(key) ) % 26
    c = data[hello_1]
    b = b + str(c)
    a = a + 1
print(f"Cipher of hello is {b}")