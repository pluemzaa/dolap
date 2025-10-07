Ckey=int(input("Enter key"))
key={0: 'a', 1: 'b', 2: 'c', 3: 'd', 4: 'e', 5: 'f', 6: 'g', 7: 'h', 8: 'i', 9: 'j', 10: 'k', 11: 'l', 12: 'm', 13: 'n', 14: 'o', 15: 'p', 16: 'q', 17: 'r', 18: 's', 19: 't', 20: 'u', 21: 'v', 22: 'w', 23: 'x', 24: 'y', 25: 'z'}
h = ((7 + Ckey)%26 ,
     (4 + Ckey)%26 ,
     (11 + Ckey)%26 ,
      (11 + Ckey)%26 ,
      (14 + Ckey)%26 ,)
print("Cipher of hello is",key[h[0]],key[h[1]],key[h[2]],key[h[3]],key[h[4]],sep = '')