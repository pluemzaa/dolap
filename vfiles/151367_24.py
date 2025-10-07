pets = input("Enter your pets:")
pets_num = {"Dog":0,"Cat":1,"Fish":2}
pets_word = "Dog,Cat,Dog,Fish,Cat"
p = pets_word.split(',')
print("Code of your pets:",pets_num[p[0]],pets_num[p[1]],pets_num[p[2]],pets_num[p[3]],pets_num[p[4]],sep='')