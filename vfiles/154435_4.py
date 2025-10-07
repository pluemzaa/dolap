message = "hello"
newMess = ""
number = 0
Key = input("Enter key")

for c in message:
  number = int(ord(c)-96)
  output = chr(((number+int(Key))%26)+96)
  newMess += output;

print("c=Cipher of hello is ", newMess)