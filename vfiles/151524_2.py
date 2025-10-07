pet_text = input("Enter your pets: ")
pet = pet_text.split(',')
data = {'Dog': 0,'Cat': 1,'Fish': 2}
ohv ={'Dog':[1,0,0],'Cat':[0,1,0],'Fish':[0,0,1]}
data1 = data[pet[0]]
data2 = data[pet[1]]
data3 = data[pet[2]]
data4 = data[pet[3]]
data5 = data[pet[4]]
print(f"Code of your pets: {code1},{code2},{code3},{code4},{code5}")
l1 = ohv[pet[0]]
l2 = ohv[pet[1]]
l3 = ohv[pet[2]]
l4 = ohv[pet[3]]
l5 = ohv[pet[4]]
print(f"One-hot vectors: \n{l1}\n{l2}\n{l3}\n{l4}\n{l5}")