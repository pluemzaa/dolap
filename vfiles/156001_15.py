key = int(input("Enter key: "))

cc = {
    0: 'a', 1: 'b', 2: 'c', 3: 'd', 4: 'e', 5: 'f', 6: 'g',
    7: 'h', 8: 'i', 9: 'j', 10: 'k', 11: 'l', 12: 'm', 13: 'n',
    14: 'o', 15: 'p', 16: 'q', 17: 'r', 18: 's', 19: 't',
    20: 'u', 21: 'v', 22: 'w', 23: 'x', 24: 'y', 25: 'z'
}

s = cc[(7 + key) % 26]
o = cc[(4 + key) % 26]
r = cc[(11 + key) % 26]
y = cc[(14 + key) % 26]

print("Cipher of hello is", s + o + r + r + y)