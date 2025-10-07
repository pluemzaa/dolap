A = {0: 'a', 1: 'b', 2: 'c', 3: 'd', 4: 'e', 5: 'f', 6: 'g', 7: 'h', 8: 'i', 9: 'j', 10: 'k', 11: 'l', 12: 'm', 13: 'n', 14: 'o', 15: 'p', 16: 'q', 17: 'r', 18: 's', 19: 't', 20: 'u', 21: 'v', 22: 'w', 23: 'x', 24: 'y', 25: 'z'}
key = int(input("Enter key"))
h = (7+key)%26
e = (4+key)%26
l = (11+key)%26
o = (14+key)%26
x = (A[h]+A[e]+A[l]+A[l]+A[o])
print ('Cipher of hello is',x)