key = int(input("Enter key"))
message = {0: 'a', 1: 'b', 2: 'c', 3: 'd', 4: 'e', 5: 'f', 6: 'g', 7: 'h', 8: 'i', 9: 'j', 10: 'k', 11: 'l', 12: 'm', 13: 'n', 14: 'o', 15: 'p', 16: 'q', 17: 'r', 18: 's', 19: 't', 20: 'u', 21: 'v', 22: 'w', 23: 'x', 24: 'y', 25: 'z'}

message1 = message[(7+(key))%26]
message2 = message[(4+(key))%26]
message3 = message[(11+(key))%26]
message4 = message[(11+(key))%26]
message5 = message[(14+(key))%26]
print("Cipher of hello is",message1,message2,message3,message4,message5)