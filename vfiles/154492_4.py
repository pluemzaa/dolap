alphabets = {0: 'a', 1: 'b', 2: 'c', 3: 'd', 4: 'e', 5: 'f', 6: 'g', 7: 'h', 8: 'i', 9: 'j', 10: 'k', 11: 'l', 12: 'm', 13: 'n', 14: 'o', 15: 'p', 16: 'q', 17: 'r', 18: 's', 19: 't', 20: 'u', 21: 'v', 22: 'w', 23: 'x', 24: 'y', 25: 'z'}
# keyboard = input()
# inv_alphabets = {(v,k) for k,v in alphabets.items()}
inv_alphabets = dict((v, k) for k, v in alphabets.items())

key = input("Enter Key")
letter = input()
cipher = list()
ikey = list()
for i in letter:
    ikey.append(inv_alphabets[i])

for i in ikey:
    cipher.append((i + int(key))%26)

ans = str()
for i in cipher:
    ans = ans + alphabets[i]

print(ans)
# h = ( 7+ int(key))%26 
# e =  (4+ int(key))%26
# l =( 11+ int(key))%26
# o =(14+ int(key))%26
# print(f"Cipher of hello is {alphabets[h]+alphabets[e]+alphabets[l]+alphabets[l]+alphabets[o]}")