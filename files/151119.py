_list = {
  "Dog":"0",
  "Cat":"1",
  "Fish":"2"
}

_list2 = {
  "Dog":[1,0,0],
  "Cat":[0,1,0],
  "Fish":[0,0,1],
}

_input = input("Enter your pets: ")
_inputSplit = _input.split(",")

a = _list[_inputSplit[0]]
b = _list[_inputSplit[1]]
c = _list[_inputSplit[2]]
d = _list[_inputSplit[3]]
e = _list[_inputSplit[4]]

text = a + "," + b + "," + c + "," + d + "," + e

print("Code of your pets:",text)
print("One-hot vectors: ")
print(_list2[_inputSplit[0]])
print(_list2[_inputSplit[1]])
print(_list2[_inputSplit[2]])
print(_list2[_inputSplit[3]])
print(_list2[_inputSplit[4]])