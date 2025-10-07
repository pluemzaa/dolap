a={0: 'a', 1: 'b', 2: 'c', 3: 'd', 4: 'e', 5: 'f', 6: 'g', 7: 'h', 8: 'i', 9: 'j', 10: 'k', 11: 'l', 12: 'm', 13: 'n', 14: 'o', 15: 'p', 16: 'q', 17: 'r', 18: 's', 19: 't', 20: 'u', 21: 'v', 22: 'w', 23: 'x', 24: 'y', 25: 'z'}
key=int(input('Enter key'))
num=[7,4,11,11,14]
cc1=a[(num[0]+key)%26]
cc2=a[(num[1]+key)%26]
cc3=a[(num[2]+key)%26]
cc4=a[(num[3]+key)%26]
cc5=a[(num[4]+key)%26]
print('cipher of hello is' ,cc1+cc2+cc3+cc4+cc5)