pet= input("Enter your pets:")
data_dict = {"Dog": 0, "Cat": 1, "Fish": 2}
_list = pet.split(',')
a = data_dict[_list[0]]
b = data_dict[_list[1]]
c = data_dict[_list[2]]
d = data_dict[_list[3]]
e = data_dict[_list[4]]
print("Code of your pets: " + str(a) + "," + str(b) + "," + str(c) + "," + str(d) + "," + str(e))