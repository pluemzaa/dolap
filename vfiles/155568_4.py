Mkey = int(input('Enter your key'))
key = {0: 'a', 1: 'b', 2: 'c', 3: 'd', 4: 'e', 5: 'f', 6: 'g', 7: 'h', 8: 'i', 9: 'j', 10: 'k', 11: 'l', 12: 'm', 13: 'n', 14: 'o', 15: 'p', 16: 'q', 17: 'r', 18: 's', 19: 't', 20: 'u', 21: 'v', 22: 'w', 23: 'x', 24: 'y', 25: 'z'}
code = ((7 + Mkey ) % 26 ,(4 + Mkey ) % 26 ,(11 + Mkey ) % 26 ,(11 + Mkey ) % 26 ,(14 + Mkey ) % 26 , )
print("Cipher of hello ",key[code[0]],key[code[1]],key[code[2]],key[code[3]],key[code[4]],sep = '')