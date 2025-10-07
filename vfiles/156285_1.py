Data = {0: 'a', 1: 'b', 2: 'c', 3: 'd', 4: 'e', 5: 'f', 6: 'g', 7: 'h', 8: 'i', 9: 'j', 10: 'k', 11: 'l', 12: 'm', 13: 'n', 14: 'o', 15: 'p', 16: 'q', 17: 'r', 18: 's', 19: 't', 20: 'u', 21: 'v', 22: 'w', 23: 'x', 24: 'y', 25: 'z'}
Key = input("Enter key")
Key = int(Key)
h = (Data[(7 + Key)%26])
e = (Data[(4 + Key)%26])
l = (Data[(11 + Key)%26])
l = (Data[(11 + Key)%26])
o = (Data[(14 + Key)%26]) 
print(f"{h}{e}{l}{l}{o}")