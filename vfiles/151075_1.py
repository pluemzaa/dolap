_list = {
  "Dog":0,
  "Cat":1,
  "Fish":2
}

_input = input("Enter your pets: ")
_inputSplit = _input.split(",")

print("Code of your pets: ",_list[_inputSplit[0]],_list[_inputSplit[1]],_list[_inputSplit[2]],_list[_inputSplit[3]],sep = ",")