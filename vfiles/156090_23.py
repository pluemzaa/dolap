alp = {
    0: 'a', 1: 'b', 2: 'c', 3: 'd', 4: 'e', 5: 'f', 6: 'g',
    7: 'h', 8: 'i', 9: 'j', 10: 'k', 11: 'l', 12: 'm', 13: 'n',
    14: 'o', 15: 'p', 16: 'q', 17: 'r', 18: 's', 19: 't',
    20: 'u', 21: 'v', 22: 'w', 23: 'x', 24: 'y', 25: 'z'
}
rev_alp = {v: k for k, v in alp.items()}
key = int(input("Enter key"))
text = "hello"
cipher = ""
for char in text:
    idx = rev_alp[char]
    shifted_idx = (idx + key) % 26
    cipher += alp[shifted_idx]
print("Cipher of hello is", cipher)