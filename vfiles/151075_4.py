_list = {
  "Dog":"0",
  "Cat":"1",
  "Fish":"2"
}

_input = input("Enter your pets: ")
_inputSplit = _input.split(",")

a = _list[_inputSplit[0]]
b = _list[_inputSplit[1]]
c = _list[_inputSplit[2]]
d = _list[_inputSplit[3]]

text = a + "," + b + "," + c + "," + d

print("Code of your pets:",text)