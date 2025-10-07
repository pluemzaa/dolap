key = int(input("Enter key"))

x = {
    0: 'a', 1: 'b', 2: 'c', 3: 'd', 4: 'e', 5: 'f', 6: 'g',
    7: 'h', 8: 'i', 9: 'j', 10: 'k', 11: 'l', 12: 'm', 13: 'n',
    14: 'o', 15: 'p', 16: 'q', 17: 'r', 18: 's', 19: 't',
    20: 'u', 21: 'v', 22: 'w', 23: 'x', 24: 'y', 25: 'z'
}

h = (7 + key) % 26
e = (4 + key) % 26
l1 = (11 + key) % 26
l2 = (11 + key) % 26
o = (14 + key) % 26

ch = x[h]
ce = x[e]
cl1 = x[l1]
cl2 = x[l2]
co = x[o]

print("Cipher of hello is", ch + ce + cl1 + cl2 + co)