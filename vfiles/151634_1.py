pet= input("Enter your pets:")
data_dict = {"Dog": 0, "Cat": 1, "Fish": 2}
_list = pet.split(',')
a = data_dict[_list[0]]
b = data_dict[_list[1]]
c = data_dict[_list[2]]
d = data_dict[_list[3]]
e = data_dict[_list[4]]
f = [a, b, c, d, e]
mklist={
    "Dog":[1,0,0],"Cat":[0,1,0],"Fish":[0,0,1]}
print("Code of your pets:", end=' ')
print(f[0],",", f[1],",", f[2],",",f[3],",",f[4])
print("One-hot vectors:")
print(mklist[_list[0]])
print(mklist[_list[1]])
print(mklist[_list[2]])
print(mklist[_list[3]])
print(mklist[_list[4]])