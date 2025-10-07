x =int(input( 'Enter Key ='))
key = {0: 'a', 1: 'b', 2: 'c', 3: 'd', 4: 'e', 5: 'f', 6: 'g', 7: 'h', 8: 'i', 9: 'j', 10: 'k', 11: 'l', 12: 'm', 13: 'n', 14: 'o', 15: 'p', 16: 'q', 17: 'r', 18: 's', 19: 't', 20: 'u', 21: 'v', 22: 'w', 23: 'x', 24: 'y', 25: 'z'}
caesar cipher =((7 + x ) % 26 
( 4 + x ) % 26,
(11 + x ) %26 ,
(11 + x ) %26 ,
(14 + x ) %26,)
print("Cipher of hello is:" , key[x[0]],key[x[1]],key[x[2]],key[x[3]],key[x[4]] ,sep='')