dict = {0: 'a', 1: 'b', 2: 'c', 3: 'd', 4: 'e', 5: 'f', 6: 'g', 7: 'h', 8: 'i', 9: 'j', 10: 'k', 11: 'l', 12: 'm', 13: 'n', 14: 'o', 15: 'p', 16: 'q', 17: 'r', 18: 's', 19: 't', 20: 'u', 21: 'v', 22: 'w', 23: 'x', 24: 'y', 25: 'z'}
key = int(input("Enter key"))

ciper = [(key + 7)%26,(key + 4)%26,(key + 11)%26,(key + 11)%26,(key + 14)%26,]

print("Cipher of hello is ",dict[ciper[0]],dict[ciper[1]],dict[ciper[2]],dict[ciper[3]],dict[ciper[4]],sep="")