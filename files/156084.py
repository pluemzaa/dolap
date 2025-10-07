cip={0: 'a', 1: 'b', 2: 'c', 3: 'd', 4: 'e', 5: 'f', 6: 'g', 7: 'h', 8: 'i', 9: 'j', 10: 'k', 11: 'l', 12: 'm', 13: 'n', 14: 'o', 15: 'p', 16: 'q', 17: 'r', 18: 's', 19: 't', 20: 'u', 21: 'v', 22: 'w', 23: 'x', 24: 'y', 25: 'z'}
A=int(input('Enter key' ))
B="Cipher of hello is "
H=cip[(7+A)%26]
E=cip[(4+A)%26]
L=cip[(11+A)%26]
O=cip[(14+A)%26]
print(B,H,E,L,L,O,sep="")


#h=7e=4l=11l=11 o=14
#split(,)