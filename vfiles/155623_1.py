Lkey = int(input("Enter key"))
key = {0: 'a', 1: 'b', 2: 'c', 3: 'd', 4: 'e', 5: 'f', 6: 'g', 7: 'h', 8: 'i', 9: 'j', 10: 'k', 11: 'l', 12: 'm', 13: 'n', 14: 'o', 15: 'p', 16: 'q', 17: 'r', 18: 's', 19: 't', 20: 'u', 21: 'v', 22: 'w', 23: 'x', 24: 'y', 25: 'z'}
Code = ((7 + Lkey) %26
            (4 + Lkey) %26
             (11 + Lkey) %26
              (14 + Lkey) %26)
print("Cipher of hello is",key[Code[0]],key[Code[1]],key[Code[3]],key[Code[4]],sep = '')