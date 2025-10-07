key=int(input("Enter Key"))
list={0: 'a', 1: 'b', 2: 'c', 3: 'd', 4: 'e', 5: 'f', 6: 'g', 7: 'h', 8: 'i', 9: 'j', 10: 'k', 11: 'l', 12: 'm', 13: 'n', 14: 'o', 15: 'p', 16: 'q', 17: 'r', 18: 's', 19: 't', 20: 'u', 21: 'v', 22: 'w', 23: 'x', 24: 'y', 25: 'z'}
x1=list[(7+(key))%26]
x2=list[(4+(key))%26]
x3=list[(11+(key))%26]
x4=list[(11+(key))%26]
x5=list[(14+(key))%26]
print(”Cipher of hello is“,x1,x2,x3,x4,x5)