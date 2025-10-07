one_hot = {
    "Dog":  [1, 0, 0],
    "Cat":  [0, 1, 0],
    "Fish": [0, 0, 1]
}
text = input("Enter your pets: ")
pets = text.split(",")
p0 = one_hot[pets[0]]
p1 = one_hot[pets[1]]
p2 = one_hot[pets[2]]
p3 = one_hot[pets[3]]
p4 = one_hot[pets[4]]
s0 = str(0)
s1 = str(1)
s2 = str(0)
s3 = str(2)
s4 = str(1)
print("Code of your pets:", s0 + "," + s1 + "," + s2 + "," + s3 + "," + s4)
print("One-hot vectors:")
print(p0)
print(p1)
print(p2)
print(p3)
print(p4)