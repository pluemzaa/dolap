data = {0: 'a', 1: 'b', 2: 'c', 3: 'd', 4: 'e', 5: 'f', 6: 'g', 7: 'h', 8: 'i', 9: 'j', 10: 'k', 11: 'l', 12: 'm', 13: 'n', 14: 'o', 15: 'p', 16: 'q', 17: 'r', 18: 's', 19: 't', 20: 'u', 21: 'v', 22: 'w', 23: 'x', 24: 'y', 25: 'z'}
data2 = {}
hello = 7 ,4 ,11 ,11 ,14 
a = 0
key = int(5)
#Caesar_cipher = ( hello[] + key ) % 26

while a <= 4 :
    hello_1 = ( hello[a] + key ) % 26
    print(a , data[hello_1])
    a = a + 1