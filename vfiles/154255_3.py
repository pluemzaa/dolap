# message="hello";alphaDict={0: 'a', 1: 'b', 2: 'c', 3: 'd', 4: 'e', 5: 'f', 6: 'g', 7: 'h', 8: 'i', 9: 'j', 10: 'k', 11: 'l', 12: 'm', 13: 'n', 14: 'o', 15: 'p', 16: 'q', 17: 'r', 18: 's', 19: 't', 20: 'u', 21: 'v', 22: 'w', 23: 'x', 24: 'y', 25: 'z'};
#   key=int(input("Enter key"))newMess = "";newMess+=

message=[7,4,11,11,14];alphaDict={0: 'a', 1: 'b', 2: 'c', 3: 'd', 4: 'e', 5: 'f', 6: 'g', 7: 'h', 8: 'i', 9: 'j', 10: 'k', 11: 'l', 12: 'm', 13: 'n', 14: 'o', 15: 'p', 16: 'q', 17: 'r', 18: 's', 19: 't', 20: 'u', 21: 'v', 22: 'w', 23: 'x', 24: 'y', 25: 'z'};key=int(input("Enter key"));newMess=alphaDict[(message[0]+key)%26];newMess+=alphaDict[(message[1]+key)%26];newMess+=alphaDict[(message[2]+key)%26];newMess+=alphaDict[(message[3]+key)%26];newMess+=alphaDict[(message[4]+key)%26];print(newMess);



# message = "hello"
# newMess = ""

# Key = input("Enter key")

# for c in message:
    
#     number = int(ord(c)-96)
#     output = chr(((number+int(Key))%26)+96)
#     newMess += output;

# print("Cipher of hello is ",newMess)